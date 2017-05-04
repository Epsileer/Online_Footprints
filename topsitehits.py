
import os, json, sys
import operator
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

data_files = os.listdir("data/history/")


hits = {}

start_year, end_year = 10000, 0

t = 0
# get the value from command line if provided
if len(sys.argv) == 2:
    t = int(sys.argv[1])

topsite = open("output/sites.txt").read().split('\n')[t]

for file_name in data_files:
    with open("data/history/" + file_name) as data_file:    
        data = json.load(data_file)
        for site in data["Browser History"]:
            address = site["url"].split('/')
            if len(address) > 2:
                if address[2] == topsite.split(", ")[0]:
                    month = datetime.fromtimestamp(site["time_usec"]/1000000).month
                    year = datetime.fromtimestamp(site["time_usec"]/1000000).year
                    if year < start_year:
                        start_year = year
                    if year > end_year:
                        end_year = year
                    m = months[month-1] + " " + str(year)
                    if m not in hits:
                        hits[m] = 1
                    else:
                        hits[m] += 1


# print(hits)
x, y = [], []
for year in range(start_year, end_year+1):
    for i in range(len(months)):
        month = months[i]
        if month + " " + str(year) in hits:
            x.append(datetime(year=year, month=i+1, day=1))
            y.append(hits[month + " " + str(year)])

fig = plt.figure()
fig.set_size_inches(16,9)
plt.plot(x, y)
plt.title(topsite.split(", ")[0])
fig.savefig("images/topsites/site" + str(t) + ".png")

