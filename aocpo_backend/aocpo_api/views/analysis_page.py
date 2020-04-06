#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.response import Response
from ..utils.BaseResponse import BaseResponse
from ..utils.database_operation import  AnalysisPageView
from .. import serializer

class GetData(AnalysisPageView):
    def get(self, response):
        res = BaseResponse()
        opt = serializer.GetData(data=response.query_params)
        if opt.is_valid():
            if self.get_users_collection.find_one({'username': opt.validated_data.get('username')}):
                data = dict()
                next_offset = opt.validated_data.get('offset') + opt.validated_data.get('limit')
                try:
                    res_data = self.get_posts_data(opt.validated_data)
                    if not res_data[3]:
                        data['is_end'] = True
                    else:
                        data['is_end'] = False
                    data['next_offset'] = next_offset
                    data['all_count'] = res_data[0]
                    data['max_date'] = res_data[1]
                    data['min_date'] = res_data[2]
                    data['posts_data'] = res_data[3]
                    res.status = 1000
                    res.msg = '成功'
                    res.data = data
                    return Response(res.get_dict)
                except Exception as err:
                    res.status = 2000
                    res.msg = '服务器异常'
                    res.error = str(err)
                    return Response(res.get_dict)
            else:
                res.status = 2004
                res.msg = '无权限'
                return Response(res.get_dict)
        else:
            res.status = 2005
            res.msg = '无效请求数据'
            return Response(res.get_dict)

class GetUserAnalyseData(AnalysisPageView):
    def get(self, response):
        res = BaseResponse()
        opt = response.query_params
        username = opt.get('username')
        if self.get_users_collection.find_one({'username': username}):
            try:
                data = self.get_users_analysis_data(opt)
                res.status = 1000
                res.msg = '成功'
                res.data = data
                return Response(res.get_dict)
            except Exception as e:
                res.status = 2000
                res.msg = '服务器异常'
                print(e)
                res.err = str(e)
                return Response(res.get_dict)
        else:
            res.status = 2004
            res.msg = '没有权限'
            return Response(res.get_dict)

class GetPostsAnalysisData(AnalysisPageView):
    def get(self, response):
        query = serializer.GetPostsAnalysisData(data=response.query_params)
        res = BaseResponse()
        if query.is_valid():
            username = query.validated_data.get('username')
            if self.get_users_collection.find_one({'username': username}):
                try:
                    data = self.get_posts_analysis_data(query.validated_data)
                    res.status = 1000
                    res.msg = '成功'
                    res.data = data
                    return Response(res.get_dict)
                except Exception as e:
                    res.status = 2000
                    res.msg = '服务器异常'
                    res.err = str(e)
                    return Response(res.get_dict)
            else:
                res.status = 2004
                res.msg = '没有权限'
                return Response(res.get_dict)
        else:
            res.status = 2005
            res.msg = '无效数据'
            return Response(res.get_dict)
