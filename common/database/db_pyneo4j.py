# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     db_pyneo4j
   Description :
   Author :       jpl
   date：          2021/10/11
-------------------------------------------------
   Change Activity:
                   2021/10/11:
-------------------------------------------------
"""
__author__ = 'Asdil'
import uuid
from py2neo import Graph, Relationship, Node


class Pyneo4j:
    """
    Neo4j类用于
    """

    def __init__(self, url, user, password, database=None):
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
        self._driver = Graph(url, auth=(user, password), name=database)
        self.database = database

    def create_node(self, labels, parameters, add_tag=False, add_uid=False):
        """create_node方法用于

        Parameters
        ----------
        labels: list
            标签列表
        parameters: dict
            参数字典
        add_tag: bool
            是否添加tag
        add_uid: bool
            是否添加uid
        Returns
        ----------
        """
        if add_tag:
            parameters['tag'] = uuid.uuid1()
        node = Node(*labels, **parameters)
        self._driver.create(node)
        if add_uid:
            uid = node.identity
            parameters['uid'] = uid
            node.update(**parameters)
            self._driver.push(node)
        return node

    def link(self, nodes, relations=None):
        """link方法用于

        Parameters
        ----------
        nodes : py2neo node list
            py2neo node列表
        relations: list or None
            属性列表

        Returns
        ----------
        """

        for i in range(len(nodes) - 1):
            try:
                r = relations.pop(0)
            except:
                r = ' '
            self._driver.create(Relationship(nodes[i], r, nodes[i + 1]))

    def is_node(self, node):
        """is_node方法用于

        Parameters
        ----------
        node : object
            节点对象或者是其它的

        Returns
        ----------
        """
        if node is Node:
            return True
        return False