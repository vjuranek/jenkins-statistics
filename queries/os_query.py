#!/usr/bin/env python

import pymongo
from pymongo import MongoClient
from collections import Counter

client = MongoClient('localhost', 27017)
stats = client.jenkins_stats.jstats

def cnt_aggregate_names(results, key_delim=" ",cnt_key="cnt"):
    items = Counter()
    for res in results:
        item = res["_id"]
        if item is None or item == "":
            item = "unknown"
        item = item.split(key_delim)[0]
        items[item] += res[cnt_key]

    total = sum(items.values())
    for item in items.most_common():
        print "%s\t...\t%d" % item + "\t{0:.0f}%".format(float(item[1])/total * 100)
    print "----------------------"
    print "All items:\t%d" % total

def os_cnt():
    os = stats.aggregate([{"$unwind":"$nodes"},{"$match":{"nodes.master":True}},{"$group":{"_id":"$nodes.os", "cnt":{"$sum":1}}},{"$sort":{"cnt":1}}])
    os = os["result"]
    cnt_aggregate_names(os)

# def plugin_cnt():
#     plugins = stats.aggregate([{"$project":{"_id":"$_id","plugins":"$plugins"}},{"$unwind":"$plugins"},{"$group":{"_id":"$plugins.name", "cnt":{"$sum":1}}},{"$sort":{"cnt":1}}])
#     plugins = plugins["result"]

# def container_cnt():
#     containers = stats.aggregate([{"$group":{"_id":"$servletContainer", "cnt":{"$sum":1}}},{"$sort":{"cnt":1}}])
#     containers = containers["result"]


os_cnt()
