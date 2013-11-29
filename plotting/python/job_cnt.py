#!/usr/bin/env python

import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats
results = stats.find({},{"jobs":1})

job_cnt = []
for res in results:
    cnt = 0
    for job_type in res["jobs"]:
        cnt += int(res["jobs"][job_type])
    # limit number of jobs, otherwise almost all stats is on one bin due to few instances with ~ 10000 slaves
    if cnt < 1000:
        #print cnt
        job_cnt.append(cnt)

n, bins, patches = plt.hist(job_cnt, 100, normed=0, histtype='step')
plt.gca().set_yscale('log')
plt.xlabel('# of jobs')
plt.ylabel('# of instances')
plt.savefig("../eps/job_cnt.eps")

