#!/usr/bin/env python
# -*- coding: utf-8 -*-
#C 1 R 0 D 3 U 2
from ..utils.database_operation import TasksManageView
from rest_framework.response import Response
from ..utils.BaseResponse import BaseResponse
from .. import serializer
import time
import json

class TaskManage(TasksManageView):

    def post(self, response):
        """
        提交任务到redis队列
        """
        _res = BaseResponse()
        _data = serializer.Task(data=response.data)
        if _data.is_valid():
            _username = response.data.get('username')
            if self.get_users_collection.find_one({'username': _username}):
                _task = json.dumps(response.data)
                try:
                    self.add_task(_task)
                    _record = dict()
                    _record['username'] = response.data.get('username')
                    _record[response.data.get('school')] = {
                                                            'running': 1,
                                                            'state': 0,
                                                            'created_date': time.strftime('%Y-%m-%d %X', time.localtime()),
                                                            'updated_date': None
                                                            }
                    self.add_task_record(_record)
                    _res.status = 1001
                    _res.msg = "任务添加成功"
                except Exception as err:
                    _res.status = 2004
                    _res.msg = str(err)
                return Response(_res.get_dict)
            else:
                _res.status = 2005
                _res.msg = "没有权限增加任务"
                return Response(_res.get_dict)
        else:
            _res.status = 2006
            _res.msg = "无效数据"
            return Response(_res.get_dict)

    def delete(self, response):
        """
        删除任务，假删除真删除
        """
        _res = BaseResponse()
        _data = serializer.DelTask(data=response.query_params)
        if _data.is_valid():
            _username = _data.validated_data.get('username')
            if self.get_users_collection.find_one({'username': _username}):
                if self.del_task(_data.validated_data):
                    _res.status = 1003
                    _res.msg = '删除成功'
                    return Response(_res.get_dict)
                else:
                    _res.status = 2003
                    _res.msg = '删除失败'
                    return Response(_res.get_dict)
            else:
                _res.status = 2004
                _res.msg = '没有权限删除'
                return Response(_res.get_dict)
        else:
            _res.status = 2005
            _res.msg = '无效数据'
            return Response(_res.get_dict)

    def put(self, response):
        _res = BaseResponse()
        _data = serializer.Task(data=response.data)
        if _data.is_valid():
            _username = response.data.get('username')
            _school = response.data.get('school')
            if self.get_users_collection.find_one({'username': _username}):
                _task = json.dumps(response.data)
                try:
                    self.add_task(_task)
                    self.modify_running({'username': _username, 'school': _school})
                    _res.status = 1002
                    _res.msg = "更新任务添加成功"
                except Exception as err:
                    _res.status = 2002
                    _res.msg = str(err)
                return Response(_res.get_dict)
            else:
                _res.status = 2004
                _res.msg = "没有权限增加更新任务"
                return Response(_res.get_dict)
        else:
            _res.status = 2005
            _res.msg = "无效数据"
            return Response(_res.get_dict)

    def get(self, response):
        """查询用户任务"""
        _res = BaseResponse()
        _username = response.query_params.get('username')
        if self.get_users_collection.find_one({'username': _username}):
            _raw_data = self.get_users_tasks(username=_username)
            if _raw_data != 'err':
                if _raw_data:
                    raw_data = list(_raw_data.items())
                    for _ in raw_data:
                        _[1]['school'] = _[0]
                    _true_data = list(map(lambda _: _[1], filter(lambda _: _[1].get('state') != -1, raw_data)))
                    _false_data = list(map(lambda _: _[1], filter(lambda _: _[1].get('state') == -1, raw_data)))
                    _res.status = 1000
                    _res.msg = '成功'
                    _res.data = {'true_data': _true_data, 'false_data': _false_data}
                    return Response(_res.get_dict)
                else:
                    _res.status = 2000
                    _res.msg = '无相关数据'
                    return Response(_res.get_dict)
            else:
                _res.status = 2004
                _res.msg = '服务器异常'
                return Response(_res.get_dict)
        else:
            _res.status = 2005
            _res.msg = '无权限'
            return Response(_res.get_dict)

class SearchSchool(TasksManageView):

    def get(self, response):
        """查询学校"""
        _res = BaseResponse()
        _word = response.query_params.get('word')
        _data = self.search_school(_word)
        if _data != 'err':
            if _data:
                _res.status = 1000
                _res.msg = '成功'
                _res.data = _data
                return Response(_res.get_dict)
            else:
                _res.status = 2000
                _res.msg = '无相关数据'
                return Response(_res.get_dict)
        else:
            _res.status = 2004
            _res.msg = '服务器异常'
            return Response(_res.get_dict)

class Recover(TasksManageView):
    """恢复假删除的任务"""
    def put(self, response):
        _opt = response.data
        _res = BaseResponse()
        if self.recover_task(_opt):
            _res.status = 1002
            _res.msg = '恢复成功'
            return Response(_res.get_dict)
        else:
            _res.status = 2002
            _res.msg = '恢复失败，服务器异常'
            return Response(_res.get_dict)




