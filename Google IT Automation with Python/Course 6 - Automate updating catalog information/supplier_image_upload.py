#!/usr/bin/env python3
import requests

url = "http://localhost/upload/"
folder = 'Course 6 - Automate updating catalog information\supplier-data\images'

# for file in folder
for file in os.listdir(folder):
    # if file is jpeg
    if file.endswith('.jpeg'):
        # open file
        with open(folder + '/' + file, 'rb') as opened:
            # send request
            r = requests.post(url, files={'file': opened})