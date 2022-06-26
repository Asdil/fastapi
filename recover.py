# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     recover
   Description :  这个是初始化定时任务模块后端数据库
   Author :       asdil
   date：          2022/5/4
-------------------------------------------------
   Change Activity:
                   2022/5/4:
-------------------------------------------------
"""
__author__ = 'Asdil'
from core import conf
from common import sqlite3_db
sqlite3_db.excute(conf.SQL_LITE6)
