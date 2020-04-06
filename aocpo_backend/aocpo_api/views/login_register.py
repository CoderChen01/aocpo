from rest_framework.response import Response
from ..utils.database_operation import MongoUsersView
from ..utils.BaseResponse import BaseResponse
from .. import serializer
from uuid import uuid4


class SignIn(MongoUsersView):
    """
    注册
    """
    def get(self, request):
        """检查用户是否存在"""
        _res = BaseResponse()
        _username = request.query_params.get("username", "")
        if self.get_users_collection.find_one({"username": _username}):
            _res.status = 2000
            _res.msg = "用户名已存在"
            return Response(_res.get_dict)
        else:
            _res.status = 1000
            _res.msg = "用户名可用"
            return Response(_res.get_dict)

    def post(self, request):
        """
        用户名密码写入数据库
        """
        _res = BaseResponse()
        _data = serializer.Users(data=request.data)
        if _data.is_valid():
            #向数据库插入数据
            _id = str(self.get_users_collection.insert(_data.validated_data))
            _res.status = 1001
            _res.msg = "注册成功"
            _res.user_id = _id
            return Response(_res.get_dict)
        else:
            _res.status = 2001
            _res.msg = "输入格式有误"
            return Response(_res.get_dict)

class Login(MongoUsersView):
    """登录"""

    def post(self, request):
        _res = BaseResponse()
        _data = serializer.Users(data=request.data)
        if _data.is_valid():
            #向数据库查询数据
            _result = self.get_users_collection.find_one(_data.validated_data, {"_id": 0})
            if _result:
                _res.status = 1000
                _res.msg = "登录成功"
                _res.nickname = _result.get("nickname", "")
                _res.username = _result.get("username", "")
                _res.aocpo_token = str(uuid4())
                return Response(_res.get_dict)
            else:
                _res.status = 2000
                _res.msg = "用户名或密码错误"
                return Response(_res.get_dict)
        else:
            _res.status = 2004
            _res.msg = "输入有误"
            return Response(_res.get_dict)




