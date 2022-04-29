# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tools
   Description :  工具库
   Author :       asdil
   date：          2022/4/29
-------------------------------------------------
   Change Activity:
                   2022/4/29:
-------------------------------------------------
"""
__author__ = 'Asdil'
import ast
import math
import datetime
from dateutil.parser import parse


def split_list(data, slice):
    """split_list方法用于拆分列表

    Parameters
    ----------
    data : list
        列表
    slice: 拆分后块大小

    Returns
    ----------
    """
    return [data[i:i + slice] for i in range(0, len(data), slice)]


def is_nan(data, is_str=False):
    """is_nan方法用于判断是不是空值

    Parameters
    ----------
    data : anytype
        任何数据类型
    is_str : bool
        是否需要考虑字符型
    Returns
    ----------
    """
    if data is None:
        return True
    if is_str:
        if type(data) is str:
            if data.lower() in {'none', 'nan'}:
                return True
    try:
        return math.isnan(data)
    except:
        return False


def combin_dic(*args):
    """combin_dic方法用于合并字典
    eg: combin_dic(d1,d2,d3....)

    Parameters
    ----------
    args : list
        字典列表
    Returns
    ----------
    """
    ret = {}
    if len(args) == 1:
        dicts = args[0]
        assert isinstance(dicts, list)  # 断言是个列表
        for _dict in dicts:
            ret = dict(ret, **_dict)
    else:
        for _dict in args:
            assert isinstance(_dict, dict)
        for _dict in args:
            ret = dict(ret, **_dict)
    return ret


def in_dict(d1, d2):
    """in_dict方法用于字典d1的key是否全在字典d2中

    Parameters
    ----------
    d1 : dict
        字典1
    d2 : dict
        字典2

    Returns
    ----------
    """
    for key in d1:
        if key in d2:
            if d1[key] != d2[key]:
                return False
        else:
            return False
    return True


def sort_key(data):
    """sort_key方法用于排序字典的key

    Parameters
    ----------
    data : dict
        字典

    Returns
    ----------
    """
    new_data = {}
    for key in sorted(data.keys()):
        new_data[key] = data[key]
    return new_data


def safe_eval(string):
    """方法用于

    Parameters
    ----------
    string : str
        需要转换的字符串

    Returns
    ----------
    """
    try:
        ret = ast.literal_eval(string)
    except:
        ret = eval(string)
    return ret


def read_json(path, encoding='UTF-8'):
    """read_json方法用于读取json文件

    Parameters
    ----------
    path : str
        json文件路径
    encoding : str
        编码类型
    Returns
    ----------
    """
    import json
    try:
        with open(path, 'r', encoding=encoding) as f:
            data = json.loads(f.read())
    except:
        with open(path, 'r') as f:
            data = json.loads(f.read())
    return data


def flatten(data):
    """flatten方法用于平铺list

    Parameters
    ----------
    data : list
        列表

    Returns
    ----------
    """
    import itertools
    return list(itertools.chain.from_iterable(data))


def inter_set(l1, l2):
    """inter_set方法用于列表交集

    Parameters
    ----------
    l1 : list or dict or set
        列表1
    l2 : list or dict or set
        列表2

    Returns
    ----------
    """
    assert type(l1) in {list, set, dict}
    assert type(l2) in {list, set, dict}
    if type(l1) is dict:
        l1 = list(l1.keys())
        l2 = list(l2.keys())
    return list(set(l1).intersection(set(l2)))


def diff_set(l1, l2):
    """diff_set方法用于列表差集

    Parameters
    ----------
    l1 : list or dict or set
        列表1
    l2 : list or dict or set
        列表2

    Returns
    ----------
    """
    assert type(l1) in {list, set, dict}
    assert type(l2) in {list, set, dict}
    if type(l1) is dict:
        l1 = list(l1.keys())
        l2 = list(l2.keys())
    return list(set(l1).difference(set(l2)))


def union_set(l1,l2):
    """union_set方法用于列表并集

    Parameters
    ----------
    l1 : list or dict or set
        列表1
    l2 : list or dict or set
        列表2

    Returns
    ----------
    """
    assert type(l1) in {list, set, dict}
    assert type(l2) in {list, set, dict}
    if type(l1) is dict:
        l1 = list(l1.keys())
        l2 = list(l2.keys())
    return list(set(l1).union(set(l2)))


def str_to_datetime(date):
    """str_to_datetime方法用于字符串转日期
    Parameters
    ----------
    date : str
        日期字符串：
        eg:
        2018-10-21
        20181021
        2018/10/21
        10-21 # 如果没有年份默认今年
        10/21
    Returns
    ----------
    datetime
    """
    return parse(date)


def datetime_to_str(date, milliseconds=False):
    """datetime_to_str方法用于日期转字符串

    Parameters
    ----------
    date : datetime
        日期
    milliseconds: bool
        是否保留毫秒
    Returns
    ----------
    """
    if milliseconds:
        return date.isoformat(sep=' ', timespec='milliseconds')
    else:
        return date.replace(microsecond=0).isoformat(' ')


def add_datetime(days=None, hours=None, minutes=None, seconds=None, weeks=None):
    """add_datetime方法用于添加datetime时间戳

    Parameters
    ----------
    days : int or None
        天数
    hours : int or None
        小时数
    minutes : int or None
        分钟数
    seconds : int or None
        秒数
    weeks : int or None
        周数

    Returns
    ----------
    """
    ret = datetime.timedelta(seconds=0)
    if days is not None:
        ret += datetime.timedelta(days=days)
    if hours is not None:
        ret += datetime.timedelta(hours=hours)
    if minutes is not None:
        ret += datetime.timedelta(minutes=minutes)
    if seconds is not None:
        ret += datetime.timedelta(seconds=seconds)
    if weeks is not None:
        ret += datetime.timedelta(weeks=weeks)
    return ret
