#! /usr/bin/env python3
import os
import requests

folder = "/data/feedback/"

# for txt file in directory, read file and add to dictionary
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        with open(folder + filename, "r") as f:
            data = f.read()
        data = data.split("\n")
        # add data to dictionary
        data_dict = {
            "title": data[0],
            "name": data[1],
            "date": data[2],
            "feedback": data[3]
        }
        # send dictionary to web service
        r = requests.post("http://104.198.201.187/feedback/", json=data_dict)
        print(r.status_code)