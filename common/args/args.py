# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     comm_args
   Description :  此处定义参数, 如果需要测试请使用测试参数
   Author :       asdil
   date：          2022/1/14
-------------------------------------------------
   Change Activity:
                   2022/1/14:
-------------------------------------------------
"""
__author__ = 'Asdil'
from pydantic import BaseModel
from typing import Union, Optional


class Args_demo(BaseModel):
    """
    Args_demo类用于参数校验
    """
    data: str


class Args_Del(BaseModel):
    """
    Args_Deljob 用于删除定时任务
    """
    job_id: str
