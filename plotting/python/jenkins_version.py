#!/usr/bin/env python

import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats
results = stats.find({},{"version":1})

versions = []
for res in results:
    versions.append(int(res["version"][2:5]))

n, bins, patches = plt.hist(versions, 50, normed=0, histtype='step')
plt.xlabel('Jenkins version')
plt.ylabel('# of instances')
plt.savefig("../eps/jenkins_version.eps")
