from PIL import Image

if __name__=='__main__':
    im=Image.open('images/Hopper.ppm')
    box=(100,100,400,400)
    region=im.crop(box)
    #region.show()
    region=region.transpose(Image.ROTATE_180)
    im.paste(region,box)
    im.show()

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
