from PIL import Image,ImageFilter

im = Image.open("images/hopper.ppm")
im = im.filter(ImageFilter.DETAIL)
#im.show()
im = im.point(lambda i: i * 0.5)
im.show()