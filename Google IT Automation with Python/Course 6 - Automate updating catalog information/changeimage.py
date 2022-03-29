# convert images from folder from 3000x2000 to 600x400 pixel, and save to jpeg
# use PIL library

# import PIL library
from PIL import Image
import os

folder = 'Course 6 - Automate updating catalog information\supplier-data\images' # use same folder for saving

for files in os.listdir(folder):
    if files.endswith('.tiff'):
        # open image
        img = Image.open(folder + '/' + files)
        # convert from RGBA to RGB
        img = img.convert('RGB')
        # resize image
        img = img.resize((600, 400))
        # save image
        img.save(folder + '/' + files.split('.')[0] + '.jpeg')

