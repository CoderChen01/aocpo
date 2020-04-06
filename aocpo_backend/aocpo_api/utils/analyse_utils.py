#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import jieba
import re
from copy import deepcopy
from logging import ERROR
jieba.setLogLevel(ERROR)

#文章类型对照表
CLASS = {
    0: '娱乐',
    1: '体育',
    2: '彩票',
    3: '房产',
    4: '教育',
    5: '时尚',
    6: '时政',
    7: '星座',
    8: '游戏',
    9: '社会',
    10: '科技',
    11: '股票',
    12: '财经',
    13: '家居'
}

#传入post对象
class phCount(object):
    """
    传入数据， 分析出用用户的手机
    """
    def __init__(self, data_iter):
        """
        初始化属性
        """
        self._data_iter = deepcopy(data_iter)

    def _gen_counter(self):
        """
        生成计数器对象， 对于每一条数据而言
        :return: 生成器
        """
        _data = (_data['device'] for _data in self._data_iter)
        for _ in _data:
            yield collections.Counter(_)

    def _result_dirty(self):
        """
        对计数器对象求和，初步生成，数据
        :return: 不符合echarts数据格式， 需进一步格式化
        """
        _result = collections.Counter()
        for _counter in self._gen_counter():
            _result += _counter
        return _result
    #对外提供接口
    def result(self):
        """
        对数据格式化， 返回echarts要求的数据格式,这里将ipad用户统一归于苹果用户
        """
        for _res_tuple in self._result_dirty().items():
            _dict = dict()
            if _res_tuple[0] == 'android':
                _dict['value'] = _res_tuple[1]
                _dict['name'] = '安卓用户'
            elif _res_tuple[0] == 'apple':
                _dict['value'] = _res_tuple[1]
                _dict['name'] = '苹果用户'
            else:
                _dict['value'] = _res_tuple[1]
                _dict['name'] = '平板用户'
            yield _dict

#传入user对象
class sexCount(object):
    """统计男女比例"""
    def __init__(self, data_iter):
        """
        初始化属性
        """
        self._data_iter = deepcopy(data_iter)

    @property
    def _sex_list(self):
        """
        封装每条数据的性别为列表
        """
        _sex_list = (data['sex'] for data in self._data_iter)
        return _sex_list

    def _result_dirty(self):
        """
        生成计数器对象
        """
        _result_dirty = collections.Counter(self._sex_list)
        return _result_dirty

    #对外接口
    def result(self):
        """
        对计数器对象结构化处理为符合echarts要求格式
        """
        for _res_tuple in self._result_dirty().items():
            _dict = dict()
            if _res_tuple[0] == 'male':
                _dict['value'] = _res_tuple[1]
                _dict['name'] = '男生'
            else:
                _dict['value'] = _res_tuple[1]
                _dict['name'] = '女生'
            yield _dict

#传入post对象,停用词词典
class contentWordCount(object):
    def __init__(self, data_iter, stopWord):
        """
        初始化属性, 加载自定义词典， 加载停用词
        """
        self._data_iter = deepcopy(data_iter)
        self._stop_word = deepcopy(stopWord)

    def _fileterStopWord(self, content_dirty):
        """
        去除停用词辅助函数
        """
        content = filter(lambda _: _ not in self._stop_word and len(_) > 1, content_dirty)
        return content

    @property
    def _content_clean(self):
        """
        经过分词， 去除停用词的内容，返回一个生成器
        """
        _content_dirty = (jieba.cut(_data['reply_content']) for _data in self._data_iter)
        return map(self._fileterStopWord, _content_dirty)

    def _gen_counter(self):
        """
        计数器生成器对象
        """
        for _ in self._content_clean:
            yield collections.Counter(_)

    @property
    def _result_dirty(self):
        """
        得到两百个热词
        """
        _result = collections.Counter()
        for _ in self._gen_counter():
            _result += _
        return iter(_result.most_common(100))

    #对外接口
    def result(self):
        """
        返回生成器
        """
        for _res_tuple in self._result_dirty:
            _dict = dict()
            _dict['value'] = _res_tuple[1]
            _dict['name'] = _res_tuple[0]
            yield _dict

#传入user对象
class nickNameWordCount(object):
    def __init__(self, data_iter):
        """
         初始化属性
        """
        self._data_iter = deepcopy(data_iter)

    @property
    def _nick_name_list(self):
        """
        所有昵称，分词后:
        """
        _nick_name = (jieba.cut(''.join(re.findall(r'[\u4e00-\u9fa5]', nk_name['name_show']))) for nk_name in self._data_iter)
        return map(lambda _nick: filter(lambda _: _ not in ['你', '我', '他', '她', '它', '的', '是', '啊', '大', '小', '了', '吧', '不', '自', '一'], _nick), _nick_name)

    def _gen_counter(self):
        """
        产生计数器对象
        :return: 生成器
        """
        for _ in self._nick_name_list:
            yield collections.Counter(_)

    @property
    def _result_dirty(self):
        """
        产生非echarts规范数据格式的数据，显示100条
        """
        _result = collections.Counter()
        for _ in self._gen_counter():
            _result += _

        return _result.most_common(100)

    #对外接口
    def result(self):
        """
        处理成echarts规范数据
        """

        for _res_tuple in self._result_dirty:
            _dict = dict()
            _dict['value'] = _res_tuple[1]
            _dict['name'] = _res_tuple[0]

            yield _dict

#传入user对象
class vipCount(object):
    """
    统计用户开通VIP状况
    """
    def __init__(self, data_iter):
        self.data_iter = deepcopy(data_iter)

    @property
    def _gen_tb_vip_list(self):
        return (_isVip['tb_vip'] for _isVip in self.data_iter)

    @property
    def _result_dirty(self):
        return collections.Counter(self._gen_tb_vip_list)

    #对外接口
    def result(self):
        """结构化数据"""
        for _res_tuple in self._result_dirty.items():
            _dict = dict()
            if _res_tuple[0]:
                _dict['value'] = _res_tuple[1]
                _dict['name'] = '会员用户'
            else:
                _dict['value'] = _res_tuple[1]
                _dict['name'] = '普通用户'
            yield _dict

#传入posts对象
class SentimentCount(object):
    """
    统计情感数量
    """
    def __init__(self, data_iter):
        """复制迭代器对象"""
        self._data_iter = deepcopy(data_iter)

    @property
    def _get_sent_list(self):
        for _ in self._data_iter:
            yield _.get('sentiment')

    @property
    def _get_dirty_counter(self):
        return collections.Counter(self._get_sent_list)

    # 对外接口
    def result(self):
        for name, value in self._get_dirty_counter.items():
            _dict = dict()
            if name == 0:
                _dict['name'] = '消极'
                _dict['value'] = value
            elif name == 1:
                _dict['name'] = '中性'
                _dict['value'] = value
            else:
                _dict['name'] = '积极'
                _dict['value'] = value
            yield _dict

# 传入posts对象
class ClassCount(object):
    """
    统计情感数量
    """

    def __init__(self, data_iter):
        """复制迭代器对象"""
        self._data_iter = deepcopy(data_iter)

    @property
    def _get_class_list(self):
        for _ in self._data_iter:
            yield _.get('classify')

    @property
    def _get_dirty_counter(self):
        return collections.Counter(self._get_class_list)

    # 对外接口
    def result(self):
        for name, value in self._get_dirty_counter.items():
            yield {'name': CLASS.get(name), 'value': value}

#加载停用词
def loadStopWord(path):
    """
    加载停用词词典
    :return:
    """
    with open(path, 'r', encoding='utf8') as f_obj:

        return list(map(lambda _: _.replace('\n', ''), f_obj.readlines()))
