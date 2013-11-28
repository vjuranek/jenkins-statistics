#!/usr/bin/env python

import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats

results = stats.aggregate([{"$unwind":"$nodes"},{"$match":{"nodes.master":True}},{"$group":{"_id":"$nodes.jvm-vendor","cnt":{"$sum":1}}}])
results = results["result"]

print results

labels = []
values = []
explode = []
EXPLODE_VAL = 0.05
for res in results:
    # skip minor vedros to have more readable plots
    if res["cnt"] > 100:
        labels.append(res["_id"])
        values.append(res["cnt"])
        explode.append(EXPLODE_VAL)

plt.pie(values, labels=labels, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.savefig("../eps/jvm_vendor.eps")
