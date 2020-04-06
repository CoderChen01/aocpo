#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapyd_api import ScrapydAPI
from .db_operations import RedisClient, MongodbClient
from . import settings
import re
import time
import json
class Middleman(object):
    def __init__(self):
        self._redis_cli = RedisClient()
        self._mongodb_cli = MongodbClient()

    @staticmethod
    def _get_scrapyd_obj_list(scrapyd_url_list):
        """
        生成scrapyd-api对象
        :param scrapyd_url_list:url列表
        :return: 列表
        """
        return map(lambda url: ScrapydAPI(url), scrapyd_url_list)

    @property
    def get_finished_spider(self):
        """
        找出所有已完成爬虫
        :return: 已完成爬虫
        """
        return filter(lambda scrapyd_obj: scrapyd_obj.list_jobs('tbSpider').get('running') == [],
                      self._get_scrapyd_obj_list(settings.SCRAPYD_LIST))

    def _send_finished_result(self, ip):
        """
        更新用户数据库中的任务完成状态
        :param ip: scrapyd主机ip
        :return:Boolean
        """
        _task = self._redis_cli.get_record(ip)
        if _task:
            _record = dict()
            _username = _task.get('username')
            _school = _task.get('school')
            _record['username'] = _username
            _record[_school] = {
                                'running': 0,
                                'state': int(self._mongodb_cli.get_task_record_state(_username, _school) )+ 1,
                                'created_date': self._mongodb_cli.get_task_record_created_date(_username, _school),
                                'updated_date': time.strftime('%Y-%m-%d %X', time.localtime())
                                }
            self._mongodb_cli.add_or_update_task_record(_record)
            return True
        else:
            return False

    def dispatch_task(self, finished_spiders, throttle):
        """
        为空闲机器分发爬虫任务
        :param finished_spiders: 空闲爬虫对象
        :return: None
        """
        _lag_task = []
        for _spider in finished_spiders:
            if _lag_task:
                _task = _lag_task.pop()
            else:
                _task = self._redis_cli.get_task
            _spider_ip = re.search('https?://(?P<ip>.*?):\d*', _spider.target).group('ip')
            self._send_finished_result(_spider_ip) #更新用户数据库结果
            if _task:
                try:
                    for _ in range(throttle):
                        _spider.schedule(settings.SCRAPYD_PROJECT_NAME, settings.SCRAPYD_SPIDER_NAME, args = json.dumps(_task))
                    self._redis_cli.add_record(_spider_ip, _task)
                    print(_spider_ip, _task)
                except Exception:
                    _lag_task.append(_task)


__all__ = ['Middleman']