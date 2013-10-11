#!/usr/bin/env python

import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats

results = stats.aggregate([{"$unwind":"$nodes"},{"$match":{"nodes.master":True}},{"$group":{"_id":{"$substr":["$nodes.jvm-version",0,5]},"cnt":{"$sum":1}}}])
results = results["result"]

labels = []
values = []
for res in results:
    labels.append(res["_id"])
    values.append(res["cnt"])
colors = ['green', 'gold', 'lightskyblue', 'red']
explode = (0.05, 0.05, 0.05, 0.05) 

plt.pie(values, labels=labels, explode=explode, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.savefig("../eps/jvm_version.eps")


