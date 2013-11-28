#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import pymongo
from pymongo import MongoClient
from collections import Counter
import matplotlib.pyplot as plt

def toFloat(num):
    try:
        return float(num)
    except:
        return 0

def toInt(num):
    try:
        return int(num)
    except:
        return 0


client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats

#results = stats.aggregate([{"$group":{"_id":{"$substr":["$version",0,5]}, "cnt":{"$sum":1}}}])
results = stats.find({},{"version":1})

versions = []
# for res in results:
#     versions.append(toFloat(res['version'][:5]))

minVal, maxVal = toInt(results.next()['version'][2:5])
for res in results:
    v  = toInt(res['version'][2:5])
    if v < minVal:
        minVal = v
    if v > maxVal:
        maxVal = v
    versions.append(v)

# versions = Counter()
# for res in results:
#     v = res["_id"]
#     versions[v] = versions[v] + res["cnt"]

# # for v in versions.most_common(10):
# #     print "%s ... %d" % (v[0],v[1])
# for v in versions:
#     print "%s ... %d" % (v,versions.get(v))

print minVal
print maxVal

plt.hist(versions, bins = range(minVal,maxVal,1), facecolor='green', alpha=0.5)
plt.xlabel('Jenkins version')
plt.ylabel('Number of instances')
plt.title(r'Jenkins versions')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()


