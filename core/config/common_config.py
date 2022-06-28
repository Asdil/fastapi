# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     common_config
   Description :
   Author :       asdil
   date：          2022/6/16
-------------------------------------------------
   Change Activity:
                   2022/6/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
import os

BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMP_DB: str = os.path.join(BASE_PATH, 'local_db/sqlite3.db')

ADD_SCHEDULER: bool = True  # 是否添加api.scheduler定时任务模块

# jwt 秘钥
# 生成新的秘钥需执行下面命令: openssl rand -hex 32
SECRET_KEY: str = "1bc1934d8c3404ea0276472a329dcc490aedc87ca4a93361b61f8e31d5d47dc0"
ALGORITHM: str = "HS256"     # 算法
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30    # 访问令牌过期分钟

# SQLITE3 初始化定时任务使用的配置
SQL_LITE1: str = 'UPDATE start_up SET pid=-1 WHERE id=? AND pid!=-1;'  # 用于控制防止多线程启动多次
SQL_LITE2: str = 'UPDATE start_up SET pid=? WHERE id=? AND pid=-1;'
SQL_LITE3: str = 'SELECT pid FROM start_up WHERE id=?;'
SQL_LITE4: str = 'SELECT password FROM jwt WHERE user=?'
SQL_LITE5: str = 'SELECT user FROM jwt WHERE user=?'
SQL_LITE6: str = 'UPDATE start_up SET pid=-1 WHERE pid!=-1;'
