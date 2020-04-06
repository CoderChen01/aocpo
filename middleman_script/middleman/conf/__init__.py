#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
class Settings(object):
    def __init__(self):
        _settings = importlib.import_module('middleman.settings')
        for setting in dir(_settings):
            if setting.isupper():
                setattr(self, setting, getattr(_settings, setting))

settings = Settings()
