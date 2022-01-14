# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     comm_args
   Description :
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


class Args_del_schedule(BaseModel):
    """
    Args_v1类用于api v1的所有参数
    """
    job_id: str