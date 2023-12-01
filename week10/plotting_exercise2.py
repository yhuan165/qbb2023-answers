#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt


df = pd.read_csv('ufo_sightings.csv')

#number of sighting in the top 5 countries (bar plot)
# image = df['country_code'].value_counts().iloc[0:5]
# indexes = image.index
# print(image)

# fig, cx = plt.subplots()

# cx.bar(indexes, image)
# cx.set_xlabel("Country Code")
# cx.set_ylabel("Number of Sightings")
# cx.set_title('Top 5 Countries and their UFO Sightings')
# fig.tight_layout()
# plt.show()

# fig.savefig("Top5Countries.png")


#sightings of ufo over time of day(lineplot)
# time = df['day_part'].value_counts()
# indexes = time.index
# print(time)
# timedf = df['day_part'].value_counts()
# print(timedf)
# orderlist = ['night','astronomical dawn','nautical dawn','civil dawn','morning','afternoon','civil dusk','nautical dusk','astronomical dusk']
# timedf = timedf.loc[orderlist]
# print(timedf)
# count = timedf.values
# fig,bx = plt.subplots()
# plt.plot(orderlist, count, color = 'green')
# bx.set_xlabel("Time of Sighting")
# bx.set_ylabel("Number of Sightings")
# bx.set_title("Number of Sightings of UFO throughout a Day")
# plt.tight_layout()
# plt.show()
# fig.savefig("sightingday.png")


#number of sighting for durations (histogram)
finaldf = df[df['duration_seconds'] < 4000]

fig, ax = plt.subplots()

ax.hist(finaldf['duration_seconds'], bins = 10)
#ax.set_xlim(0, 1000000)
ax.set_xlabel("Reported Duration (seconds)")
ax.set_ylabel("Number of Sighting")
ax.set_title("Distribution of Duration of UFO Sightings")
fig.tight_layout()
plt.show()

fig.savefig("Duration.png")