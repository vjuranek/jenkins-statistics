#!/usr/bin/env python

import re
import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats

results = stats.aggregate([{"$match":{"version":re.compile("\d\.\d+\.\d")}},{"$group":{"_id":{"$substr":["$version",0,7]},"cnt":{"$sum":1}}}])
results = results["result"]
print results

labels = []
values = []
explode = []
EXPLODE_VAL = 0.05
for res in results:
    print "%s ... %s"%(res["_id"],res["cnt"])
    # make plot more readable
    if res["cnt"] > 100:
        labels.append(res["_id"])
        values.append(res["cnt"])
        explode.append(EXPLODE_VAL)

plt.pie(values, labels=labels, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.savefig("../eps/lts_version.eps")
