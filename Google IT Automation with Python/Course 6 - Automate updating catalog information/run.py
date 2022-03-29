#! /usr/bin/env python3
import os
import requests
import json

folder = "supplier-data/descriptions/"
url = "http://34.132.133.99/fruits/"

# for txt file in directory, read file and add to dictionary
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        with open(folder + filename, "r") as f:
            data = f.read()
        data = data.split("\n")
        # extracting the first line and removing the newline
        name = data[0].strip('\n')
        # extracting the second line and removing the newline and lbs. Also changing it to integer
        weight = int(data[1].strip('\n').strip(' lbs'))
        # extracting the third line and removing the newline
        description = data[2].strip('\n')
        # add image file name to dict
        image_name = filename.strip('.txt') + '.jpeg'
        # add data to dictionary
        data_dict = {
            "name": name,
            "weight": weight,
            "description": description,
            "image_name": image_name
        }
        #print(data_dict)
        # converting dictionary to json
        dict_to_json = json.dumps(data_dict)
        # Creating headers to push the data to fruits url
        header = {'Content-Type': 'application/json'}
        # pushing data to fruits url
        r = requests.post(url, headers=header, data=dict_to_json)
        # print response code
        print(r.status_code)