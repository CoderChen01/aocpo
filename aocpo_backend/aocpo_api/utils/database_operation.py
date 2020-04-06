#!/usr/bin/env python
# -*- coding: utf-8 -*-
#第三方
import pymongo
import redis
from django.conf import settings
from rest_framework.views import APIView
#内部提供
import os
from uuid import uuid4
from time import mktime, strptime, strftime, localtime
#自定义
from ..utils import analyse_utils

class MongoView(APIView):
    """
    封装mongodb数据库的操作
    """
    def __init__(self):
        super().__init__()
        self._client = pymongo.MongoClient(settings.MONGO_URI)

    def get_collection(self, db_name, collection_name):
        _db = self._client[db_name]
        return _db[collection_name]

    def del_collection(self, db_name, collection_name):
        _db = self._client[db_name]
        _db.drop_collection(collection_name)

class RedisView(APIView):
    """
    封装redis相关操作
    """
    def __init__(self):
        """
        连接数据库
        """
        super().__init__()
        pool = redis.ConnectionPool.from_url(settings.REDIS_URL)
        self._db = redis.StrictRedis(connection_pool=pool)

    def add_task(self, task):
        """
        增加用户任务
        :param task:用户任务
        :return: 成功与否
        """
        return self._db.lpush(settings.REDIS_QUEUE_NAME, task)

class MongoUsersView(MongoView):
    """
    用户数据库
    """
    @property
    def get_users_collection(self):
        return self.get_collection(settings.MONGO_DATABASE_USERS,
                            settings.MONGO_DATABASE_USERS_COLLECTION)

class MongoTasksView(MongoView):
    """
    操作用户数据库的任务
    """
    def add_task_record(self, record):
        """
        增加任务记录
        :param record:
        :return:
        """
        self.get_collection(settings.MONGO_DATABASE_USERS,
                            settings.MONGO_DATABASE_USERS_TASKS_COLLECTION)\
            .update_one({"username": record.get('username')},{"$set": record}, True)

    def del_task(self, opt):
        """
        删除任务，分为真删除与假删除
        :param opt:
        :return:
        """
        _username = opt.get('username')
        _school = opt.get('school')
        _isDel = opt.get('isDel')
        if _isDel:
            _base_posts_name = '{school}-posts-{username}'
            _base_users_name = '{school}-users-{username}'
            try:
                self.del_collection(settings.MONGO_DATABASE_TIEBADATA,
                                    _base_posts_name.format(school = _school, username = _username))
                self.del_collection(settings.MONGO_DATABASE_TIEBADATA,
                                    _base_users_name.format(school=_school, username=_username))
                up = self.get_collection(settings.MONGO_DATABASE_USERS,
                                         settings.MONGO_DATABASE_USERS_TASKS_COLLECTION)\
                    .find_one({'username': _username},{_school: 0})
                self.get_collection(settings.MONGO_DATABASE_USERS,
                                    settings.MONGO_DATABASE_USERS_TASKS_COLLECTION)\
                    .find_one_and_replace({'username': _username},up)
                return True
            except Exception:
                return False

        else:
            try:
                _up = self.get_collection(settings.MONGO_DATABASE_USERS,
                                          settings.MONGO_DATABASE_USERS_TASKS_COLLECTION)\
                    .find_one({'username': _username},{_school: 1})
                _up_data = {
                    _school: {
                        'running': _up.get(_school).get('running'),
                        'state': -1,
                        'created_date': _up.get(_school).get('created_date'),
                        'updated_date': _up.get(_school).get('updated_date'),
                        'deleted_state': _up.get(_school).get('state')
                    }
                }
                self.get_collection(settings.MONGO_DATABASE_USERS,
                                    settings.MONGO_DATABASE_USERS_TASKS_COLLECTION)\
                    .update_one({'username': _username},{'$set': _up_data})
                return True
            except Exception:
                return False

    def recover_task(self, opt):
        """恢复假删除的任务"""
        _username = opt.get('username')
        _school = opt.get('school')
        try:
            _up = self.get_collection(settings.MONGO_DATABASE_USERS,
                                      settings.MONGO_DATABASE_USERS_TASKS_COLLECTION).find_one({'username': _username},
                                                                                               {_school: 1})
            _up_data = {
                        _school: {
                                  'running': _up.get(_school).get('running'),
                                  'state': _up.get(_school).get('deleted_state'),
                                  'created_date': _up.get(_school).get('created_date'),
                                  'updated_date': _up.get(_school).get('updated_date')
                                  }
                        }
            self.get_collection(settings.MONGO_DATABASE_USERS,
                                settings.MONGO_DATABASE_USERS_TASKS_COLLECTION).update_one({'username': _username},
                                                                                                    {'$set': _up_data})
            return True
        except Exception:
            return False

    def search_school(self, word):
        """
        根据关键字检索学校
        :param word:
        :return:
        """
        _school_col = self.get_collection(settings.MONGO_DATABASE_SCHOOLDATA, settings.MONGO_DATABASE_SCHOOL_COLLECTION)
        _regex_base = '.*?{_word}.*?'
        try:
            _data = _school_col.find({'school': {'$regex': _regex_base.format(_word = word)}}, {'_id':0})
            return list(_data)
        except Exception as err:
            return 'err'

    def get_users_tasks(self, username):
        """
        获取用户数据中的任务记录
        :param username:
        :return:
        """
        try:
            _data = self.get_collection(settings.MONGO_DATABASE_USERS,
                                settings.MONGO_DATABASE_USERS_TASKS_COLLECTION)\
                .find_one({'username': username},{'_id': 0, 'username': 0})
            return _data
        except Exception:
            return 'err'

    def modify_running(self, opt):
        """修改运行状态"""
        _username = opt.get('username')
        _school = opt.get('school')
        _up = self.get_collection(settings.MONGO_DATABASE_USERS,
                                  settings.MONGO_DATABASE_USERS_TASKS_COLLECTION)\
            .find_one({'username': _username},{_school: 1})
        _up_data = {
            _school: {
                'running': 1,
                'state': _up.get(_school).get('state'),
                'created_date': _up.get(_school).get('created_date'),
                'updated_date': _up.get(_school).get('updated_date')
            }
        }
        self.get_collection(settings.MONGO_DATABASE_USERS,
                            settings.MONGO_DATABASE_USERS_TASKS_COLLECTION)\
            .update_one({'username': _username},{'$set': _up_data})

class MongoDataView(MongoView):
    def get_posts_data(self, opt):
        """信息汇总页面数据请求"""
        base_col_name = '{school}-posts-{username}'
        #查询条件
        username = opt.get('username')
        school = opt.get('school')
        order = opt.get('order', -1)
        classify = opt.get('classify', 2000)
        sentiment = opt.get('sentiment', 2000)
        date_start = opt.get('date_start', 2000)
        date_end = opt.get('date_end', 2000)
        #限制条件
        offset = opt.get('offset')
        limit = opt.get('limit')
        #查参数 (判断顺序不能变，因为涉及到索引问题）
        query_params = dict()
        if date_start != 2000 and date_end != 2000:
            _start = int(mktime(strptime(date_start, '%Y-%m-%d %X')))
            _end = int(mktime(strptime(date_end, '%Y-%m-%d %X')))
            query_params['date'] = {'$gte': _start, '$lte': _end}
        if classify != 2000:
            query_params['classify'] = classify
        if sentiment != 2000:
            query_params['sentiment'] = sentiment

        #查数据
        col_name = base_col_name.format(school=school, username=username)
        col = self.get_collection(settings.MONGO_DATABASE_TIEBADATA, col_name)
        all_count = col.count_documents(query_params)
        if all_count:
            max_date = list(col.find(query_params, {'date': 1, '_id': 0}).sort([('date',  -1)]).limit(1))[0].get('date')
            min_date = list(col.find(query_params, {'date': 1, '_id': 0}).sort([('date', 1)]).limit(1))[0].get('date')
            posts_data = list(col.find(query_params, {'_id': 0, 'device': 0, 'reply_content': 0, 'reply_num': 0}).sort([('date', order)]).limit(limit).skip(offset))
            for _ in posts_data:
                _['date'] = strftime('%Y-%m-%d %X', localtime(_.get('date')))
                _['url'] = 'http://tieba.baidu.com/p/' + _.get('tid')
                try:
                    _['author_url'] = 'http://tieba.baidu.com/home/main?un=' + _.get('author_name')
                except Exception:
                    _['author_url'] = None
                _['key'] = str(uuid4())
        else:
            max_date =None
            min_date = None
            posts_data = None
        return all_count, max_date, min_date, posts_data
    def get_users_analysis_data(self, opt):
        """用户分析组件请求"""
        username = opt.get('username')
        school = opt.get('school')
        col_users_name = f'{school}-users-{username}'
        col_posts_name = f'{school}-posts-{username}'

        col = self.get_collection(settings.MONGO_DATABASE_TIEBADATA,col_users_name)
        #活跃用户数据统计
        active_users_data = dict()
        active_users = list(col.find().sort([('post_num', -1)]).limit(10))
        active_users_data['x_data'] = list(map(lambda _: _.get('user_name'), active_users)) #列表
        active_users_data['y_data'] = list(map(lambda _: _.get('post_num'), active_users)) #列表

        #新老用户数据统计
        old_users_count = col.count_documents({'tb_age': {'$gte': 1}})
        new_users_count = col.count_documents({'tb_age': {'$lt': 1}})
        new_old_data = [
            {'name': '新用户', 'value': new_users_count},
            {'name': '老用户', 'value': old_users_count}
        ]

        #粉丝多的用户
        famous_users_data = dict()
        famous_users = list(col.find().sort([('fans', -1)]).limit(10))
        famous_users_data['x_data'] = list(map(lambda _: _.get('user_name'), famous_users))  # 列表
        famous_users_data['y_data'] = list(map(lambda _: _.get('fans'), famous_users))  # 列表

        #vip, 男女比例, 昵称常用词， 机型比例，s数据总量

        data_iter = col.find()
        #vip
        vip_count = analyse_utils.vipCount(data_iter)
        vips_data = list(vip_count.result()) #饼图

        #n男女比例
        sex_count = analyse_utils.sexCount(data_iter)
        sex_data = list(sex_count.result())  #饼图

        #昵称常用词
        nick_name_count = analyse_utils.nickNameWordCount(data_iter)
        nick_name_data = list(nick_name_count.result()) #饼图

        #机型比例
        _iter = self.get_collection(settings.MONGO_DATABASE_TIEBADATA,col_posts_name).find()
        ph_count = analyse_utils.phCount(_iter)
        device_data = list(ph_count.result())

        # 数据总量
        all_count = len(list(data_iter))

        data = dict()
        data['all_count'] = all_count
        data['active_users_data'] = active_users_data
        data['new_old_data'] = new_old_data
        data['famous_users_data'] = famous_users_data
        data['vips_data'] = vips_data
        data['sex_data'] = sex_data
        data['nick_name_data'] = nick_name_data
        data['device_data'] = device_data
        return  data
    def get_posts_analysis_data(self, opt):
        """获取帖子分析数据"""
        username = opt.get('username')
        school = opt.get('school')
        days = opt.get('days', 10)
        date_start = opt.get('date_start', 2000)
        date_end = opt.get('date_end', 2000)


        col_name = f'{school}-posts-{username}'

        col = self.get_collection(settings.MONGO_DATABASE_TIEBADATA, col_name)

        query_params = dict()
        if date_start != 2000 and date_end != 2000:
            query_params['date'] = {'$gte': date_start, '$lte': date_end}

        if query_params:
            #数据量
            all_count = col.count_documents({})
            current_all_count = col.count_documents(query_params)

            #热度帖子
            hot_posts_data = dict()
            hot_posts = col.find(query_params, {'_id': 0}).sort([('reply_num', -1)]).limit(10)
            hot_posts_data['x_data'] = list(range(1, 11))
            hot_posts_data['y_data'] = list(map(lambda _: {'name': _.get('tid'), 'value': _.get('reply_num')}, hot_posts))

            #用与数据分析的数据
            data_iter = col.find(query_params, {'_id': 0})

            #帖子热词
            stop_words = analyse_utils.loadStopWord(os.path.join(settings.BASE_DIR, 'data/stopWords.txt'))
            hot_words_count = analyse_utils.contentWordCount(data_iter, stop_words)
            hot_words_data = list(hot_words_count.result())

            #文章类型统计
            class_count = analyse_utils.ClassCount(data_iter)
            class_count_data = list(class_count.result())

            #情感类型统计
            sent_class_count = analyse_utils.SentimentCount(data_iter)
            sent_class_data = list(sent_class_count.result())

            data = dict()
            data['all_count'] = all_count
            data['current_all_count'] = current_all_count
            data['hot_posts_data'] = hot_posts_data
            data['hot_words_data'] = hot_words_data
            data['class_count_data'] = class_count_data
            data['sent_class_data'] = sent_class_data

            return data

        #没有自定义时间范围时执行
        else:
            # 数据总量
            all_count = col.count_documents({})

            #时间范围
            max_date = list(col.find({}, {'date': 1, '_id': 0}).sort([('date', -1)]).limit(1))[0].get('date')
            min_date = list(col.find({}, {'date': 1, '_id': 0}).sort([('date', 1)]).limit(1))[0].get('date')

            #默认7天内数据
            start = max_date - days * 24 * 60 * 60
            end = max_date
            data_iter = col.find({'date': {'$gte': start, '$lte': end}}, {'_id': 0})

            #当前数据量
            current_all_count = col.count_documents({'date': {'$gte': start, '$lte': end}})

            # 帖子热词
            stop_words = analyse_utils.loadStopWord(os.path.join(settings.BASE_DIR, 'data/stopWords.txt'))
            hot_words_count = analyse_utils.contentWordCount(data_iter, stop_words)
            hot_words_data = list(hot_words_count.result())
            # 文章类型统计
            class_count = analyse_utils.ClassCount(data_iter)
            class_count_data = list(class_count.result())
            # 情感类型统计
            sent_class_count = analyse_utils.SentimentCount(data_iter)
            sent_class_data = list(sent_class_count.result())

            #热帖
            hot_posts_data = dict()
            hot_posts = col.find({'date': {'$gte': start, '$lte': end}}, {'_id': 0}).sort([('reply_num', -1)]).limit(10)
            hot_posts_data['x_data'] = list(range(1, 11))
            hot_posts_data['y_data'] = list(map(lambda _: {'name': _.get('tid'), 'value': _.get('reply_num')}, hot_posts))

            data = dict()
            data['max_date'] = max_date
            data['min_date'] = min_date
            data['all_count'] = all_count
            data['current_all_count'] = current_all_count
            data['hot_posts_data'] = hot_posts_data
            data['hot_words_data'] = hot_words_data
            data['class_count_data'] = class_count_data
            data['sent_class_data'] = sent_class_data

            return data


class TasksManageView(RedisView, MongoTasksView, MongoUsersView):
    pass

class AnalysisPageView(MongoDataView, MongoUsersView):
    pass
