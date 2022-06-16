# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     development_config
   Description :  用于测试环境参数配置
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
import os
from core.config.common_config import *
# 生产模式配置
DEBUG: bool = True
# 项目文档
TITLE: str = "FastAPI项目文档"
DESCRIPTION: str = "这是一个FastAPI标准模板"

ADD_SCHEDULER = False  # 是否添加api.scheduler定时任务模块



