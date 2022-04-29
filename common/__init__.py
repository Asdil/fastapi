# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
from .logger import logger
from .args import comm_args
from .database.db_sqlit3 import Sqlit3
sqlite3_db = Sqlit3()
