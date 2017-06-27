#Nicole and John's modified image
from PIL import *
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path
import PIL.ImageDraw
from PIL import ImageFilter
from PIL import Image

import sys
from PIL import Image
im = Image.open("son6.JPG")


box = (750,750,1400,1400) #Rotated180 and 270,blurred,emobssed,grey scaled
region = im.crop(box)
region = region.transpose(Image.ROTATE_270).filter(ImageFilter.BLUR)
#im1 = im.filter(ImageFilter.BLUR)
im.paste(region, box)
im.save('son7.JPG')
im.show()
