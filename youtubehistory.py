import os, json

titles = open("output/youtubetitles.txt", "w")

data_files = os.listdir("data/youtube/watch/")
for file_name in data_files:
    with open("data/youtube/watch/" + file_name) as data_file:    
        data = json.load(data_file)
        for watch in data:
            titles.write(clean(watch["snippet"]["title"]) + "\n")