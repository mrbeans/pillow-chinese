from PIL import Image

if __name__=='__main__':
    im=Image.open('images/Hopper.ppm')
    r,g,b=im.split()
    im=Image.merge('RGB',(r,b,g))
    im=im.resize((256,256))
    im=im.rotate(45)
    im.show()

