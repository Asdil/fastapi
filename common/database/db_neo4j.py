# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     neo4j
   Description :
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
from neo4j import GraphDatabase


class Neo4j:
    """
    Neo4j类用于连接执行neo4j相关命令
    """
    def __init__(self, url, user, password, database):
        """__init__(self):方法用于

        Parameters
        ----------
        url: str
            neo4j服务器地址
        user: str
            用户名
        password: str
            密码
        database : str or None
            数据了名称
        Returns
        ----------
        """
        self._driver = GraphDatabase.driver(url, auth=(user, password))
        self.database = database

    def close(self):
        """close方法用于关闭连接
        """
        self._driver.close()

    def _cypher_run(self, session, cypher, rtype='data'):
        """_cypher_run方法用于执行命令

        Parameters
        ----------
        session : neo4j session
            neo4j 会话 不用显示传递
        cypher : str
            Cypher 语句, neo4j 专用的sql语句
        rtype : str
            返回值种类 data 或者 graph
            如果选择graph
                可使用 graph._nodes.values() 或者 graph._relationships.values()
                将相关信息取出来
        Returns
        ----------
        """
        result = session.run(cypher)

        if rtype == 'data':  # 返回数据
            result = result.data()
        elif rtype == 'graph':  # 返回图
            result = result.graph()
        else:
            result = None
        return result

    def run(self, cypher, rtype='data'):
        """run方法用于

        Parameters
        ----------
        cypher : str
            Cypher 语句, neo4j 专用的sql语句
        rtype : str
            返回值种类 data 或者 graph
            如果选择graph
                可使用 graph._nodes.values() 或者 graph._relationships.values()
                将相关信息取出来 提取时需要使用list()函数
        Returns
        ----------
        """
        result = None
        if self.database:
            with self._driver.session(database=self.database) as session:
                if ' return ' in cypher or ' RETURN ' in cypher:
                    result = session.read_transaction(self._cypher_run, cypher=cypher, rtype=rtype)  # 查询操作
                else:
                    session.write_transaction(self._cypher_run, cypher=cypher, rtype=rtype)  # 写操作
        else:
            with self._driver.session() as session:
                if ' return ' in cypher or ' RETURN ' in cypher:
                    result = session.read_transaction(self._cypher_run, cypher=cypher, rtype=rtype)  # 查询操作
                else:
                    session.write_transaction(self._cypher_run, cypher=cypher, rtype=rtype)  # 写操作
        return result

