# -*- coding: utf-8 -*-
import pymongo
from .items import postDataItem, authorDataItem
import json
from urllib.parse import urlencode
import requests
class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db, pre_url):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.predictor_url = pre_url
        self._client = None
        self._db = None
        self._school_post = None
        self._school_user = None


    @classmethod
    def from_crawler(cls, crawler):
        """
        实例化数据库
        """
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
                   mongo_db=crawler.settings.get('MONGO_DATABASE'),
                   pre_url=crawler.settings.get('PREDICTOR_URL'))

    def open_spider(self, spider):
        """
        创建集合对象
        """
        _args = json.loads(spider.args)
        self._school_post = _args.get('school') + '-' + 'posts' + '-' + _args.get('username')
        self._school_user = _args.get('school') + '-' + 'users' + '-' + _args.get('username')
        self._client = pymongo.MongoClient(self.mongo_uri) #连接数据库
        self._db = self._client[self.mongo_db]
        #创建索引
        self._db[self._school_post].create_index([('date', pymongo.ASCENDING),
                                                  ('classify', pymongo.ASCENDING),
                                                  ('sentiment', pymongo.ASCENDING)], name='all')
        self._db[self._school_post].create_index([ ('classify', pymongo.ASCENDING),
                                                  ('sentiment', pymongo.ASCENDING)], name='two')
        self._db[self._school_post].create_index([('sentiment', pymongo.ASCENDING)], name='one')

        self._db[self._school_user].create_index([('post_num', pymongo.ASCENDING)])
        self._db[self._school_user].create_index([('fans', pymongo.ASCENDING)])
        self._db[self._school_user].create_index([('tb_age', pymongo.ASCENDING)])

    def close_spider(self, spider):
        """
        爬虫关闭是同时关闭数据库
        """
        self._client.close()

    def process_item(self, item, spider):
        """
        判断属于什么数据，存取到对应数据库
        """
        if isinstance(item, postDataItem):
            content = item.get('content')
            title = item.get('title')
            pre_data = content if content != '' else title
            request_data = urlencode({'data': pre_data})
            url = self.predictor_url + request_data
            response = requests.get(url)
            try:
                print('预测内容中。。。。。。')
                results = response.json()
            except Exception:
                return item
            item['sentiment'] = results.get('data').get('sentiment')
            item['classify'] = results.get('data').get('classify')
            self._db[self._school_post].update_one({'tid':item.get('tid')}, {'$setOnInsert':item}, True)
        elif isinstance(item, authorDataItem):
            print('获得用户信息', dict(item))
            self._db[self._school_user].update_one({'user_name':item.get('user_name')}, {'$setOnInsert':item}, True)
        return item
