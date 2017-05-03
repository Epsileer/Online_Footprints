import matplotlib.pyplot as plt
import numpy as np


websites = open("output/sites.txt").read().splitlines()[:50]


F = 0
urls, frequencies = [], []
for w in websites:
    tup = w.split(', ')
    url, frq = tup[0], int(tup[1])
    urls.insert(len(urls), url)
    frequencies.insert(len(frequencies), frq)
    F += frq


purls, pfrequencies = [], []
f = 0
for i in range(len(urls)):
    if frequencies[i]/F >= 0.007:
        f += frequencies[i]
        purls.insert(len(purls), urls[i])
        pfrequencies.insert(len(pfrequencies), frequencies[i])
    else:
        purls.insert(len(purls), "others")
        pfrequencies.insert(len(pfrequencies), F-f)
        break           



# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = purls
sizes = pfrequencies
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
fig1.set_size_inches(18,14)
patches, texts = ax1.pie(sizes, labels=labels, shadow=False, startangle=50)
for i in range(len(texts)):
    texts[i].set_fontsize(20)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig1.savefig("images/history.png")