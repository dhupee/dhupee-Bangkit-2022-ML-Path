from PIL import Image
import os

# open folder with images
folder = "/home/student-03-c0282a86fc41/images"
folder_target = "/opt/icons/"

# for each image in folder
for filename in os.listdir(folder):
    # rotate image 90 degrees clockwise and resize to 128x128
    img = Image.open(os.path.join(folder, filename))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.rotate(90).resize((128, 128))
    # save image to new folder in jpeg format
    img.save(os.path.join(folder_target, filename), "jpeg")