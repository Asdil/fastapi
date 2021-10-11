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

        Returns
        ----------
        """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 200,
            'message': message,
            'data': data,
            **kwargs
        })
    )


def resp_201(**kwargs) -> Response:
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


def resp_500(message: str) -> UnicornException:
    """resp_500方法用于服务器遇到错误，无法完成请求

        Parameters
        ----------
        message : str
            错误信息

        Returns
        ----------
        """
    return UnicornException(500, message)


def resp_400(message: str) -> UnicornException:
    """resp_400方法用于内部验证数据错误

        Parameters
        ----------
        message : str
            错误信息
        Returns
        ----------
        """
    return UnicornException(400, message)
