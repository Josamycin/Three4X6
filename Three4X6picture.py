# Python Program to make an image for three four-by-six prints at store like CVS or Walgreens
# The penultimate line of this program should be updated to refer to the desired filepath

import tkinter as tk
from tkinter import filedialog

from PIL import Image

image1path = filedialog.askopenfilename()
image2path = filedialog.askopenfilename() 
image3path = filedialog.askopenfilename()

image1 = Image.open(image1path)
image2 = Image.open(image2path)
image3 = Image.open(image3path)

def aspect_ratio(image):
    ratio = image.width/image.height
    return ratio

# print ('image1 aspect ratio: ' + str(aspect_ratio(image1)))
# print ('image2 aspect ratio: ' + str(aspect_ratio(image2)))
# print ('image3 aspect ratio: ' + str(aspect_ratio(image3)))

def rotate_image(image):
    rotated_image = image.transpose(Image.ROTATE_90)
    return rotated_image

def crop_image(image,left, top, right, bottom):
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image

def scale_image(image,width,height):
    scaled_image = image.resize((width,height), Image.LANCZOS)
    return scaled_image

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

if aspect_ratio(image1) > 1:
    image1rotate = rotate_image(image1)
else:
    image1rotate = image1
    
if aspect_ratio(image2) > 1:
    image2rotate = rotate_image(image2)
else:
    image2rotate = image2
    
if aspect_ratio(image3) > 1:
    image3rotate = rotate_image(image3)
else:
    image3rotate = image3

image1crop = crop_image(image1rotate,(image1rotate.width-image1rotate.height*(2/3))/2,0,image1rotate.height*(2/3) + (image1rotate.width-image1rotate.height*(2/3))/2,image1rotate.height)
image2crop = crop_image(image2rotate,(image2rotate.width-image2rotate.height*(2/3))/2,0,image2rotate.height*(2/3) + (image2rotate.width-image2rotate.height*(2/3))/2,image2rotate.height)
image3crop = crop_image(image3rotate,(image3rotate.width-image3rotate.height*(2/3))/2,0,image3rotate.height*(2/3) + (image3rotate.width-image3rotate.height*(2/3))/2,image3rotate.height)

image1scale = scale_image(image1crop,min(image1crop.width,image2crop.width,image3crop.width),min(image1crop.height,image2crop.height,image3crop.height))
image2scale = scale_image(image2crop,min(image1crop.width,image2crop.width,image3crop.width),min(image1crop.height,image2crop.height,image3crop.height))
image3scale = scale_image(image3crop,min(image1crop.width,image2crop.width,image3crop.width),min(image1crop.height,image2crop.height,image3crop.height))

image1image2 = get_concat_h(image1scale, image2scale)
image1image2image3 = get_concat_v(image1image2, rotate_image(image3scale))
# image1image2image3.save(r'<Output Path>')
image1image2image3.show()