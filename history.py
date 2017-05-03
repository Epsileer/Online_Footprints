import os, json
import operator

websites = open("output/sites.txt", "w")

data_files = os.listdir("data/history/")

website_freq = {}

for file_name in data_files:
    with open("data/history/" + file_name) as data_file:    
        data = json.load(data_file)
        for site in data["Browser History"]:
            address = site["url"].split('/')
            if len(address) > 2:
                if address[2] in website_freq:
                    website_freq[address[2]] += 1
                else:
                    website_freq[address[2]] = 1

sorted_website_freq = reversed(sorted(website_freq.items(), key=operator.itemgetter(1)))
for website in sorted_website_freq:
    websites.write(website[0] + ": " + str(website[1]) + "\n")