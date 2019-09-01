from PIL import Image

if __name__=='__main__':
    im=Image.open('images/Hopper.ppm')
    im=im.transpose(Image.ROTATE_90)
    im.show()

