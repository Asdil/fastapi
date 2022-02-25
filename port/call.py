# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     call
   Description :
   Author :       asdil
   date：          2022/2/25
-------------------------------------------------
   Change Activity:
                   2022/2/25:
-------------------------------------------------
"""
__author__ = 'Asdil'
import json
import http.client


def split_url(url):
    """split_url方法用于分解url

    Parameters
    ----------
    url : str
        接口地址

    Returns
    ----------
    """
    # re.findall(r'(\d+\.\d+\.\d+\.\d+):(\d+)/(.+)', url)
    url = url.split('//')[-1]
    address, port = url.split(':')
    port = port.split('/')[0]
    path = url[len(address) + len(port) + 1:]
    port = int(port)
    return address, port, path


def post(url, data, headers=None, decode='utf-8'):
    """post方法用于post接口

    Parameters
    ----------
    data: dict
        post数据
    headers: dict or None
        头文件
    decode: str
        文件解码种类 eg utf-8， gbk， gbk123
    Returns
    ----------
    """
    url, port, path = split_url(url)
    conn = http.client.HTTPConnection(url, port)
    payload = json.dumps(data)
    if headers is None:
        headers = {
            'Content-Type': 'application/json'
        }
    conn.request("POST", path, payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode(decode)
    data = json.loads(data)
    return data, res.status


def get(url, data=None, headers=None, decode='utf-8'):
    """get方法用于get接口

    Parameters
    ----------
    url : str
        get接口地址
    data: dict or None
        内容数据
    headers: dict or None
        头文件
    decode: str
        解码格式

    Returns
    ----------
    """
    url, port, path = split_url(url)
    conn = http.client.HTTPConnection(url, port)
    if data is None:
        data = ''
    if headers is None:
        headers = {}
    conn.request("GET", path, data, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode(decode)
    return data, res.status
