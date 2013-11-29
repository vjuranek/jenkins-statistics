#!/usr/bin/env python

import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats
results = stats.find({},{"nodes":1})

slave_cnt = []
for res in results:
    # limit number of slaves, otherwise almost all stats is on one bin due to few instances with ~ 1000 slaves
    if len(res["nodes"]) < 100:
        slave_cnt.append(len(res["nodes"]))

n, bins, patches = plt.hist(slave_cnt, 100, normed=0, histtype='step')
plt.gca().set_yscale('log')
plt.xlabel('# of slaves')
plt.ylabel('# of instances')
plt.savefig("../eps/slave_cnt.eps")
