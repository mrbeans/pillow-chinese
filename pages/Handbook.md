# 使用手册

## 预览

<b>Python Imaging Library（PIL）</b>给你的Python解释器提供了处理图片的能力

PIL提供了对多种格式的图片进行高效且非常强大的处理能力。

PIL的核心库设计之初是为了快速访问常见的图片格式，所以他相对于一般的图片处理程序提供了更强大的功能

我们来看看这个库的一些可能用途。

### 图片存档

PIL一开始是为了图片存档和批处理程序使用。你可以利用PIL进行创建缩略图，转换图片格式，打印图片等操作

而现在的PIl则可以标记和读取多种格式的图片，创建/修改的操作则被故意限制为只支持常用的格式。

### 图片展示

最新的发布版本包含了Tkinter模块的<b>`PhotoImage`</b>和<b>`BitmapImage`</b>接口，以及可以在PythonWin和其他基于Windows的工具包下可以使用的<b>`Windows DIB interface`</b>。

为了方便调试，我们提供了<b>`show()`</b>方法将图片存储之后再调用其他程序将其显示出来。

### 图片处理

PIL提供了图片处理的基础能力，包括点操作，使用一组内置卷积内核进行过滤，以及色彩空间的转换。

同时，它也支持重置图片尺寸、翻转以及任意角度的旋转

有一种柱状图方法可以让你从图像中提取一些统计数据。这可以用于自动增强对比度，并用于全局统计分析。

## 教程

### 使用Image类

PIL中最重要的类就是<b>`Image`</b>类，在模块中也是一样的名字。有很多种方式可以创建<b>`Image`</b>类的实例；比如加载一张图片文件，处理其他图片或者是从0创建一张空白图片。

可以使用<b>`Image`</b>模块中的<b>`open()`</b>方法加载图片文件：

```Python
>>> from PIL import Image
>>> im=Image.open("hopper.ppm")
```

如果读取成功，open方法将会返回一个<b>`Image`</b>对象，现在你可以通过实例的属性来检查文件内容：

```Python
>>> print(im.format,im.size,im.mode)
PPM (512,512) RGB
```

属性<b>`format`</b>标记了文件的源格式，如果图片不是从文件中读取的，那属性就会返回<b>`None`</b>。<b>`size`</b>属性返回的是一个包含了宽高（以像素为单位）的2个元素的元组。<b>`mode`</b>属性定义了图像中波段的数量和名称以及像素的类型和深度，通常情况下，“L”（亮度）表示灰度图，“RGB”表示彩色图，“CMYK”表示预打印图片（印刷色彩模式）。

如果图片打开失败，会抛出<b>`IOError`</b>异常。

一旦你创建了<b>`Image`</b>类的实例，你就可以使用PIL提供的方法来处理图片。比如，显示我们刚才加载的图片：

```Python
>>> im.show()
```

> 标准版本中的<b>`show()`</b>方法效率比较低，因为他要将图片临时保存并且调用应用程序来显示图片。如果你的机器上没有安装可以显示图片的程序，<b>`show()`</b>方法会不起作用。如果可以显示图片，那么就可以极大地提高调试和测试的效率。

以下部分<b>简要的描述</b>了此库中提供的其他功能。

### 图片的读写

PIL支持多种图片格式，如果需要从磁盘读取图片可以使用<b>`Image`</b>模块中的<b>`open()`</b>方法，你无需关注要打开的文件的格式，PIL会根据文件内容自动识别。

保存图片可以使用<b>`Image`</b>模块中的<b>`save()`</b>方法，对于保存操作来说，文件名字是很重要的。如果你不指定要保存的文件格式，PIL会根据文件名字的后缀自动的将图片转换成对应的格式。

#### 将图片转换成JPEG格式

```Python
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
```

<b>`save`</b>方法的第二个参数告诉PIL文件要保存的格式，如果文件名没有后缀，就必须要指明文件的格式（译者注：第二个参数以字符串的形式提供文件格式即可，不区分大小写，因为save方法内部会统一调用upper方法将其转成大写，如：“PPM”，“PNG”，“JPEG”）：

```Python
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f
    if infile != outfile:
        try:
            Image.open(infile).save(f,"PNG")
        except IOError:
            print("cannot convert", infile)
```

#### 创建JPEG的缩略图

```Python
import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)
```

需要说明的是，除非真的需要，否则PIL不会解码或者加载[栅格数据](https://baike.baidu.com/item/%E6%A0%85%E6%A0%BC%E6%95%B0%E6%8D%AE/5261386)，当你打开文件的时候，PIL就会从文件头中读取文件格式、类型、尺寸等其他解码需要的属性，但是文件的其余部分知道你需要处理的时候才会被加载。

这也是为什么PIL读取图片文件很快，因为他不受文件大小和压缩类型影响。

#### 标识图像文件

```Python
import sys
from PIL import Image

for infile in sys.argv[1:]:
    try:
        with Image.open(infile) as im:
            print(infile, im.format, "%dx%d" % im.size, im.mode)
    except IOError:
        pass
```

### 剪切，粘贴，合并图片

<b>`Image`</b>类提供了区域选择的方法，使用<b>`crop()`</b>方法可以从图片中截取一个子矩形

##### 从图片中复制一个子矩形

```python
box=(100,100,400,400)
region=im.crop(box)
```

通过一个长度为4的元组定义你要截取的区域，他们的意义分别是（左，上，右，下）。PIL把图片的左上角作为坐标系的原点(0,0)。另外请注意，坐标指的是像素之间的位置，所以上图截取的是一个尺寸为300x300的正方形区域。

现在可以以某种方式处理截取的区域并粘贴回去。

#### 对子矩形做处理之后再粘贴回去

```Python
region=region.transpose(Image.ROTATE_180)
im.paste(regin,box)
```

当把选区粘贴回去的时候，选区的尺寸必须和给定区域完全匹配。此外，该区域也不能超出图像。然而，原始图片和选区的图片格式却不必完全一致。如果不一致，在选区被粘贴回去之前会被自动的转换成和原始图片一致的格式。(更多详细信息可以参阅[颜色变换](https://pillow.readthedocs.io/en/latest/handbook/tutorial.html#color-transforms)的部分)。`译者注：比如从图片A中截取了区域B，粘贴到图片C上，上述的‘原始图片’指的就是C，选区指的是B`

这里有另外一个例子：

#### 翻转图片

```Python
def roll(image, delta):
    """Roll an image sideways."""
    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image
```

更高级的技巧，`paste`方法有一个可选参数用于处理粘贴图片的透明度，255表示粘贴的选区完全不透明（即把选区不做任何透明度的处理粘贴上去），而0则表示粘贴的图片是完全透明的（看起来和没有粘贴一样），0-255中间值表示了不同的透明度。比如：粘贴RGBA图像并将其用作遮罩将粘贴图像的不透明部分，但不粘贴其透明背景

#### 颜色的分割与合并

## 概念

## 附录
<b>``</b>