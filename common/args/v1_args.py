# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     args_v
   Description :
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
from pydantic import BaseModel
from typing import Union, Optional


class Args_v1(BaseModel):
    """
    Args_v1类用于api v1的所有参数
    """
    data1: Optional[str] = None
    data2: float
    data3: Union[str, float]
