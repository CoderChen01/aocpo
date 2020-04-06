#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import settings
import json
import redis
import pymongo

class RedisClient(object):
    """
    封装redis相关操作
    """
    def __init__(self):
        """
        连接数据库
        """
        pool = redis.ConnectionPool.from_url(settings.REDIS_URL)
        self._db = redis.StrictRedis(connection_pool=pool)

    @property
    def get_task(self):
        """
        取数据
        :return:数据
        """
        _task = self._db.rpop(settings.REDIS_QUEUE_NAME)
        if _task:
            return json.loads(_task)
        else:
            return _task

    def add_task(self, task):
        """
        增加用户任务
        :param task:用户任务
        :return: 成功与否
        """
        return self._db.lpush(settings.REDIS_QUEUE_NAME, task)

    @property
    def queue_length(self):
        """
        队列长度
        :return:length
        """
        return self._db.llen(settings.REDIS_QUEUE_NAME)

    def add_record(self, ip, task):
        """
        增加获取记录
        :param ip:
        :param task: object
        :return:
        """
        task = json.dumps(task)
        return self._db.hset(settings.REDIS_RECORD_NAME, ip, task)

    def get_record(self, ip):
        """
        获取对应ip的记录
        :param ip: scrayd地址
        :return: 对应任务
        """
        _task = self._db.hget(settings.REDIS_RECORD_NAME, ip)
        if _task:
            if _task != b'null':
                self._db.hset(settings.REDIS_RECORD_NAME, ip, 'null')
            return json.loads(_task)
        else:
            return _task

    @property
    def get_record_length(self):
        """
        返回正在进行中任务数量
        :return: int
        """
        return self._db.hlen(settings.REDIS_RECORD_NAME)

    @property
    def get_record_tasks(self):
        """
        返回正在进行中的任务
        :return: 任务列表
        """
        return map(lambda val: json.loads(val.decode('utf8')), self._db.hvals(settings.REDIS_RECORD_NAME))

    @property
    def get_record_ips(self):
        """
        返回运行中的主机ip
        :return:list
        """
        return map(lambda _key: _key.decode('utf8'), self._db.hkeys(settings.REDIS_RECORD_NAME))


    def del_record(self, ip):
        """
        删除一条记录
        :param ip: xrapyd所在机器ip
        :return: Boolean
        """
        return self._db.hdel(settings.REDIS_RECORD_NAME, ip)

class MongodbClient(object):
    def __init__(self):
        """
        拿到集合操作对象
        """
        self._client = pymongo.MongoClient(settings.MONGO_URI)
        self._db = self._client[settings.MONGO_DATABASE_USERS]
        self.collection = self._db[settings.MONGO_DATABASE_USERS_SPIDERS_TASKS_COLLECTION]

    def add_or_update_task_record(self, record):
        """
        增加或更新任务记录
        :param record: {"username": "18175006085", "school1": {'state': 1, 'create_date': ..., 'updated_date': ...}}
        :return:
        """
        try:
            self.collection.update_one({"username": record.get('username')}, {"$set": record}, True)
            return True
        except Exception as err:
            return err

    def get_task_record_state(self, username, school):
        return self.collection.find_one({"username": username}, {school: 1}).get(school).get('state')

    def get_task_record_created_date(self, username, school):
        return self.collection.find_one({"username": username}, {school: 1}).get(school).get('created_date')

__all__ = ['RedisClient', 'MongodbClient']
