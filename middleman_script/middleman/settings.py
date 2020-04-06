#!/usr/bin/env python
# -*- coding: utf-8 -*-

#配置scrapyd的URI：scrapyd_list = [{},{}..] 如：scrapyd_list = [ 'http://192.168.68.128:6800']
SCRAPYD_LIST = [ 'http://192.168.68.128:6800']
SCRAPYD_PROJECT_NAME = 'tbSpider'
SCRAPYD_SPIDER_NAME = 'tbSpider'


#配置redis的地址，unique = True 格式：redis://[:password]@localhost:6379/db
REDIS_URL = 'redis://192.168.68.128:6379/1'

#设置redis中队列， 记录的键名
REDIS_QUEUE_NAME = 'tasks_queue'
REDIS_RECORD_NAME = 'fetch_record'

#mongodb设置
MONGO_URI = 'mongodb://192.168.68.128:27017'
MONGO_DATABASE_USERS = 'users'
MONGO_DATABASE_USERS_SPIDERS_TASKS_COLLECTION = 'users_spiders_tasks'