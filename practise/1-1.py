from PIL import Image
im=Image.open('images/Hopper.ppm')
print(im.format,im.size,im.mode)
im.show()