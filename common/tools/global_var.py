# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     global_var
   Description :   用于全局变量
   Author :        Asdil
   date：          2020/11/5
-------------------------------------------------
   Change Activity:
                   2020/11/5:
-------------------------------------------------
"""
__author__ = 'Asdil'


def __init():
    """__init方法用于初始化

    Parameters
    ----------
    param : str

    Returns
    ----------
    """
    global __global_dict
    __global_dict = {}


def get(key, val=None):
    """get方法用于取出参数

    Parameters
    ----------
    key : str
        变量名称
    val : None
        没有找到时返回的
    Returns
    ----------
    """
    if key not in __global_dict:
        return val
    return __global_dict[key]


def set(key, value):
    """set方法用于保存变量

    Parameters
    ----------
    key : str or dict
        变量名或者字典
    value : anytype
        变量值
    Returns
    ----------
    """
    if type(key) is dict:
        for k in key:
            del __global_dict[k]  # 先删除
            __global_dict[k] = key[k]
    else:
        if key in __global_dict:
            del __global_dict[key]  # 先删除
        __global_dict[key] = value


def keys():
    """keys方法用于获取所有变量名

    Parameters
    ----------
    Returns
    ----------
    """
    return list(__global_dict.keys())


__init()
