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
# 生产模式配置
DEBUG: bool = True
# 项目文档
TITLE: str = "FastAPI项目文档"
DESCRIPTION: str = "这是一个FastAPI标准模板"

BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMP_DB: str = os.path.join(BASE_PATH, 'local_db/sqlite3.db')

ADD_SCHEDULER = True  # 是否添加api.scheduler定时任务模块

# SQLITE3 初始化定时任务使用的配置
SQL_LITE1 = 'UPDATE start_up SET pid=-1 WHERE id=1 AND pid!=-1;'
SQL_LITE2 = 'UPDATE start_up SET pid=? WHERE id=1 AND pid=-1;'
SQL_LITE3 = 'SELECT pid FROM start_up WHERE id=1;'

