#!/usr/bin/env python
# -*- coding: utf-8 -*-
class BaseResponse(object):
    def __init__(self):
        self.status = None
        self.msg = None

    @property
    def get_dict(self):
        return self.__dict__