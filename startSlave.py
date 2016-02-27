# -*- coding: utf-8 -*-

import setting
from spider.collector import CollectWorkManager
from spider.crawler import CrawlWorkManager
try:
    import cPickle as pickle
except ImportError:
    import pickle
import redis
import time


if __name__=="__main__":
    global proxylist
    proxylist = []
    client = redis.Redis(host=setting.REDIS_SERVER, port=setting.REDIS_PORT, password=setting.REDIS_PW, db=0)
    redisproxylist = client.get("PROXYLIST")
    if redisproxylist != None:
        proxylist = redisproxylist
    work_manager =  CrawlWorkManager(setting.SLAVE_CRAWLER_NUM)
    collect_work_manager =  CollectWorkManager(setting.SLAVE_COLLECTOR_NUM)

    while True:
        time.sleep(10)
        redisproxylist = client.get("PROXYLIST")
        if redisproxylist != None:
            proxylist = redisproxylist
        else:
            proxylist = []

