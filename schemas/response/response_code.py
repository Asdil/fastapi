# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     response_code
   Description :  统一响应状态码
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
from typing import Union
from fastapi import status
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

"""返回值代码及其具体含义
200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
204 NO CONTENT - [DELETE]：用户删除数据成功。
400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。
"""


class UnicornException(Exception):
    """UnicornException用于异常类,直接抛出异常"""
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        # self.data = None


def resp_200(*, data: Union[list, dict, str] = None, message: str = "Success", **kwargs) -> Response:
    """resp_200方法用于200(请求成功)，服务器已成功处理了请求。 通常，这表示服务器提供了请求的网页

        Parameters
        ----------
        data : list or dict or str
            返回的数据
        message : str
            提示信息

        Returns
        ----------
        """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'status_code': 200,
            'message': message,
            'data': data,
            **kwargs
        })
    )


def resp_200_udf(**kwargs) -> Response:
    """resp_200方法用于200(请求成功)，服务器已成功处理了请求。 通常，这表示服务器提供了请求的网页

        Parameters
        ----------
        data : list or dict or str
            返回的数据

        Returns
        ----------
        """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            **kwargs
        })
    )


def resp_fail_udf(message: str) -> UnicornException:
    """resp_udf方法用请求失败自定义返回

        Parameters
        ----------
        message : str
            错误信息

        Returns
        ----------
        """
    return UnicornException(500, message)


def resp_500(*, data: str = None, message: str = "服务器发生错误，无法判断发出的请求是否成功") -> Response:
    """resp_500方法用于500错误(服务器端出现问题)，INTERNAL SERVER ERROR 服务器发生错误，用户将无法判断发出的请求是否成功。

            Parameters
            ----------
            data : list or dict or str
                返回的数据
            message : str
                提示信息

            Returns
            ----------
            """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'code': 500,
            'message': message,
            'data': data,
        }
    )


def resp_400(*, data: str = None, message: str = "用户发出的请求有错误") -> Response:
    """resp_500方法用于400错误(请求有问题)，用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的

            Parameters
            ----------
            data : list or dict or str
                返回的数据
            message : str
                提示信息

            Returns
            ----------
            """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 400,
            'message': message,
            'data': data,
        }
    )