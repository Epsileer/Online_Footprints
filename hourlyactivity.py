import os, json, sys
import operator
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

data_files = os.listdir("data/history/")

hourly_activity = [0 for x in range(24)]

for file_name in data_files:
    with open("data/history/" + file_name) as data_file:    
        data = json.load(data_file)
        for site in data["Browser History"]:
        	hourly_activity[datetime.fromtimestamp(site["time_usec"]/1000000).hour-1] += 1

fig, ax = plt.subplots()
plt.title("Hourly Activity")
ax.set_xlabel('Hours (24)')
ax.set_ylabel('Website Hits')
rects = ax.bar([x + 0.5 for x in range(24)], hourly_activity, 0.92, color='b')
fig.savefig("images/hourlyactivity.png")