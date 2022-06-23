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


class Args1(BaseModel):
    """
    Args1 类用于示空白参数
    """
    data: Optional[str] = None


class Args2(BaseModel):
    """
    Args2 用于使用job_id删除 apscheduler 指定定时任务
    """
    job_id: str
