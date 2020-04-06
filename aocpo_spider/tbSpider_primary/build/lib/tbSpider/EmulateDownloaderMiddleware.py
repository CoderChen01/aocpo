#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
class Emulate(object):
    def __init__(self):
        self.ua = UserAgent(use_cache_server=False)
    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.ua.random
        return None
