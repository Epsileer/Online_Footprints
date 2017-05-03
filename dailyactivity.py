import os, json, sys
import operator
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

data_files = os.listdir("data/history/")

daily_activity = [0 for x in range(7)]

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for file_name in data_files:
    with open("data/history/" + file_name) as data_file:    
        data = json.load(data_file)
        for site in data["Browser History"]:
        	daily_activity[datetime.fromtimestamp(site["time_usec"]/1000000).weekday()] += 1

fig, ax = plt.subplots()
plt.title("Daily Activity")
ax.set_xlabel('Weekdays')
ax.set_ylabel('Website Hits')
rects = ax.bar([x for x in range(7)], daily_activity, 0.9, color='g', tick_label=days)
fig.savefig("images/dailyactivity.png")