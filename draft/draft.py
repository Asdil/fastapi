# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     draft
   Description :
   Author :       fibrizoasdil
   date：          2022/6/26
-------------------------------------------------
   Change Activity:
                   2022/6/26:
-------------------------------------------------
"""
__author__ = 'Asdil'
from common import tools


def args(n: int):
    for j in range(n):
        yield j


def f(arg):
    return arg + 1

data = args(100)
print(type(data))
ret = tools.parallel(data, f, 2, 0, 1)
print(ret)
