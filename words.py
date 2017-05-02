# Generates a text file containing the list of words that you searched
# That file can be subsequently used by wordclouds.py to generate wordclouds
# Author: Pranshu Gupta

import os, json
from pprint import pprint

data_files = os.listdir("data/")

for file_name in data_files:
    with open("data/" + file_name) as data_file:    
        data = json.load(data_file)
        for event in data["event"]:
            print(event["query"]["query_text"])
