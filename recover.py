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
from common import sqlite3_db
SQL_LITE1 = 'UPDATE start_up SET pid=-1 WHERE id=1 AND pid!=-1;'
sqlite3_db.excute(SQL_LITE1)