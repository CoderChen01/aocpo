#!/usr/bin/env python
# -*- coding: utf-8 -*-
from middleman.midlleman_main import Middleman
import time

def monitor(period, throttle):
    """
    监听、分发任务
    :param period: 轮询周期
    :param throttle: 一台机器爬虫运行数量
    :return:
    """
    while True:
        try:
            middleman = Middleman()
            _finished_spider = middleman.get_finished_spider
            if _finished_spider:
                middleman.dispatch_task(_finished_spider, throttle)
        except Exception as e:
            print(e)
            continue
        time.sleep(period *  60)