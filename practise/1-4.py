import os,sys
from PIL import Image

def roll(img, delta):
    """Roll an image sideways."""
    image=Image.open(img)
    xsize, ysize = image.size
    print(image.size)
    
    delta = int(delta) % xsize
    print(delta)
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))

    return image

if __name__=='__main__':
    img,delta=sys.argv[1:]
    im=roll(img,delta)
    im.show()