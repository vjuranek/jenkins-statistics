#!/usr/bin/env python

import pymongo
from pymongo import MongoClient
from collections import Counter
import matplotlib.pyplot as plt

client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats

results = stats.aggregate([{"$unwind":"$nodes"},{"$match":{"nodes.master":True}},{"$group":{"_id":"$nodes.os", "cnt":{"$sum":1}}},{"$sort":{"cnt":1}}])

results = results["result"]
os_stat = Counter()
for res in results:
    os = res["_id"]
    if os is None:
        os = "unknown"
    os = os.split()[0]
    os_stat[os] = os_stat[os] + res["cnt"]

for os in os_stat:
    print "%s ... %d" % (os, os_stat.get(os))


# labels = []
# values = []
# for os in os_stat.most_common(4):
#     labels.append(os)
#     values.append(os_stat.get(os))

# print labels
# print values

# colors = ['green', 'gold', 'lightskyblue', 'red']
# explode = (0.05, 0.05, 0.05, 0.05) 

# plt.pie(values, labels=labels, explode=explode, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=90)
# # Set aspect ratio to be equal so that pie is drawn as a circle.
# plt.axis('equal')
# plt.savefig("../eps/os.eps")

