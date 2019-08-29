# 安装

## 注意事项

> Pillow 和 PIL 在同一个环境下不可共存，安装 Pillow 之前请先卸载 PIL；

> Pillow 1.0（包含） 版本之后不再支持通过“import Image”的方式进行引用，请使用“from PIL import Image”作为替代；

> Pillow 2.1.0（包含） 版本之后不再支持“import _imaging”，请使用“from PIL.Image import core as _imaging”替代。

## 说明

> Pillow对不同Python版本的支持度

|        Python        |  2.4  |  2.5  |  2.6  |  2.7  |  3.2  |  3.3  |  3.4  |  3.5  | 3.6 | 3.7 |
|  ------------------  | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | --- | --- |
|    Pillow < 2.0.0    |  Yes  |  Yes  |  Yes  |  Yes  |       |       |       |       |     |     |
|   Pillow 2.x - 3.x   |       |       |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |     |     |
|      Pillow 4.x      |       |       |       |  Yes  |       |  Yes  |  Yes  |  Yes  | Yes |     |
| Pillow 5.0.x - 5.1.x |       |       |       |  Yes  |       |       |  Yes  |  Yes  | Yes |     |
| Pillow 5.2.x - 5.4.x |       |       |       |  Yes  |       |       |  Yes  |  Yes  | Yes | Yes |
|      Pillow 6.x      |       |       |       |  Yes  |       |       |       |  Yes  | Yes | Yes |
|   Pillow >= 7.0.0    |       |       |       |       |       |       |       |  Yes  | Yes | Yes |


## 基本安装

> 下面的步骤介绍的Pillow安装方式，只可以处理最常用的图片格式，如果需要查看完整的支持列表，请查看“[扩展类库](https://pillow.readthedocs.io/en/latest/installation.html#external-libraries)”

使用pip安装Pillow

```Python
$ pip install Pillow
```

### Windows安装

为了支持python的maxtri,我们为windows的32和64位系统提供了.whl,.egg和可执行安装包的方式的Pillow的二进制版本,如果需要使用Raqm功能，则需要额外安装libraqm,fribidi,和harfbuzz

```Python
>> pip install Pillow
```

### macOS安装

我们为macOS上的每一个版本都提供了whl格式的二进制包，这些二进制包里面包含了出libimagequant以外的所有可选类库，如果需要使用Raqm功能，则需要额外安装libraqm,fribidi,和harfbuzz

```Python
$ pip install Pillow
```

### Linux安装

我们为Linux上的每一个版本都提供了whl格式的二进制包，这些二进制包里面包含了出libimagequant以外的所有可选类库，如果需要使用Raqm功能，则需要额外安装libraqm,fribidi,和harfbuzz

```Python
$ pip install Pillow
```

对于大多数主要的Linux发行版本，如：Fedora，Debian/Ubuntu和ArchLinux，PIL中已经包含Pillow，比如：``python-imaging``

### FreeBSD安装

Pillow可以通过官方Ports或者Packages的方式安装在FreeBSD系统上：

<b>Ports方式：</b>

```Python
$ cd /usr/ports/graphics/py-pillow && make install clean
```

<b>Packages方式：</b>

```Python
$ pkg install py27-pillow
```

[Pillow FreeBSD port](https://www.freshports.org/graphics/py-pillow/) 和packages的安装方式已经由``ports团队``在所有支持的FreeBSD版本上针对Python 2.7和3.x测试通过

## 从源码构建

从 [PyPI](https://pypi.org/project/Pillow/) 下载并解压文件

### 外部类库

> 如果只需要使用Pillow的基础功能<b>并不需要安装额外的依赖包</b>，默认只需要安装<b>Zlib</b>和<b>libjpeg</b>

> 一些操作系统已经在名为``depends``的目录下包含了安装依赖项所需要的脚本。同时，这些脚本也可以从``docker镜像仓库``的Dockerfiles中获取。

Pillow的很多功能都需要额外的依赖包：

* <b>libjpeg</b> 提供了操作JPEG的功能
    * Pillow已经在libjpeg 6b,8,9-9c版本以及libjpeg-turbo 8的版本上测试通过
    * libjpeg已经成为Pillow 3.0.0之后版本的默认依赖项，但是也可以通过``--disable-jpeg``参数禁用
* <b>zlib</b> 提供压缩PNG的能力
    * zlib已经成为Pillow 3.0.0之后版本的默认依赖项，但是也可以通过``--disable-zlib``参数禁用
* <b>libtiff</b> 提供了压缩TIFF的功能
    * Pillow已经在libtftt 3.x和4.0版本下测试通过
* <b>libfreetype</b> 提供了类型相关的服务
* <b>littlecms</b> 提供了颜色处理的能力
    * Pillow 2.2.1以及之前的版本使用了liblcms1，而Pillow 2.3.0以后的版本使用的是liblcms2，且已经在1.19和2.7-2.9的版本上测试通过
* <b>libwebp</b> 提供了对WebP格式的支持
    * Pillow在不支持透明WebP文件的0.1.3版本上测试通过，而0.3.0之后的版本才支持处理透明图片
* <b>tcl/tk</b> 提供了对tkinter位图和照片的支持
* <b>openjpeg</b> 提供了操作JPEG 2000(.jp2)的功能
    * Pillow已经在openjpeg 2.0.0,2.1.0和2.3.1版本下通过测试
    * Pillow不支持和Debian Jessie一起被跳过的早期的1.5系列
* <b>libimagequant</b> 提供了提升色彩量化的能力
    * Pillow已经在libimagequant 2.6-2.12.5版本下测试通过
    * Libimagequant基于的GPLv3协议比Pillow的**协议多了更多限制，因此我们无法提供libimagequant的二进制文件
    * Windows支持：Libimagequant需要使用VS2015/MSVC 19编译，所以在Windows下的Python 2.7版本不支持Libimagequant
* <b>libraqm</b> 提供了复杂文本布局的支持
    * libraqm提供了双向文本支持(通过使用FriBiDi),形状处理(使用HarfBuzz)，以及合适的项目化脚本，总之，Raqm支持Unocode编码下的大多数写作系统
    * libraqm依赖于以下类库：FreeType，HarfBuzz，FriBiDi，在安装libraqm之前应该确保你已经安装了上述依赖包
    * 如果没有安装libraqm将不能设置文本的字体和方向。
    * 如果你已经安装了libraqm和他的所有依赖项，Pillow 5.0.0以后的版本在你需要的时候会自动加载libraqm
    * Windows支持性：目前Raqm还不支持Windows平台

如果你已经安装了以上依赖项，执行：

```Python
$ pip install Pillow
```

如果依赖项已经安装到了你机器上的标准库目录下（比如：`/usr`或者是`/usr/local`），就不需要再进行额外的配置。如果依赖项被自定义安装到了非标准位置，那么你需要在`setup.py`或`setup.cfg`文件中配置安装工具以支持这些位置，或者是通过命令行工具将他们添加到环境变量中：

```Python
$ CFLAGS="-I/usr/pkg/include" pip install pillow
```

如果Pillow已经在没有依赖项的情况下编译通过，那么你必须手动清除pip缓存或者是通过使用`--no-cache-dir`选项使用新安装的外部依赖强制构建无缓存的编译。

### 编译选项

* 环境变量：`MAX_CONCURRENCY=n`.Pillow可以使用多线程编译扩展，配置项`MAX_CONCURRENCY`用于设置使用多少CPU核心进行编译，将值设置为1则禁用并行编译。`MAX_CONCURRENCY`的默认值是4，如果CPU没有4核，则会使用所有的核心。
* 编译选项：`--disable-zlib`，`--disable-jpeg`，`--disable-tiff`，`--disable-freetype`，`--disable-lcms`，`--disable-webp`，`--disable-webpmux`，`--disable-jpeg2000`，`--disable-imagequant`。以上参数可以跳过编译相应的功能模块，即使开发库在当前机器上已经存在
* 编译选项：`--enable-zlib`，`--enable-jpeg`，`--enable-tiff`，`--enable-freetype`，`--enable-lcms`，`--enable-webp`，`--enable-webpmux`，`--enable-jpeg2000`，`--enable-imagequant`。要求需要编译相关的功能模块，如果这些类库在当前机器上不存在则会抛出错误，Webpmux（WebP metadata）依赖于WebP支持。Tcl和TK同样必须同时使用。
* 编译选项`--disable-platform-guessing`。将会跳过`include`和`library`目录的所有平台的相关猜测，用于在环境变量中配置正确路径的自动构建系统（比如：`Buildroot`）
* 编译选项：`--debug`。会给`include`和`library搜索处理`打上调试标记，以转储所有的搜索路径并且输出到控制台

使用举例：

```Python
$ MAX_CONCURRENCY=1 python setup.py build_ext --enable-[feature] install
```
或者使用pip：
```Python
$ pip install pillow --global-option="build_ext" --global-option="--enable-[feature]"
```


### 在macOS上编译

### 编译选项
### 在macOS上编译
### 在Windows上编辑
### 在FreeBSD上编译
### 在Linux上编译
### 在安卓上编译

## 平台支持性

### 持续集成计划
### 其他平台

## 旧版本