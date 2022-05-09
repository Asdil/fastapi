# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     hello_world
   Description :
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
from common import logger
from common.args.args import *
from schemas.response import response_code


def pipeline_v1(args, host):
    """pipeline方法用于

    Parameters
    ----------
    args: Args1
        参数包
    host: str
        请求参数地址

    Returns
    ----------
    """
    data = args.data
    return response_code.resp_200(data=data)


