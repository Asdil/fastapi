# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     db_sqlit3
   Description :
   Author :       jpl
   date：          2021/10/11
-------------------------------------------------
   Change Activity:
                   2021/10/11:
-------------------------------------------------
"""
__author__ = 'Asdil'
import sqlite3
from core import conf


class Sqlit3():
    """
    Sqlit3类用于存储临时数据
    """
    def __init__(self):
        """__init__(self):方法用于
        """
        self.drive = sqlite3.connect(conf.TEMP_DB)

    def select(self, sql):
        """excute方法用于

        Parameters
        ----------
        sql : str
            sql查询语句

        Returns
        ----------
        """
        ret = self.drive.execute(sql)
        ret = ret.fetchall()
        return ret

    def excute(self, sql):
        """excute方法用于

        Parameters
        ----------
        sql: str
            sql语句

        Returns
        ----------
        """
        self.drive.execute(sql)
        self.drive.commit()
