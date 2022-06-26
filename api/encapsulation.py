# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     v1_encapsulation
   Description :  用于封装调用函数
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'

from common import *
from fastapi import Depends
from api import pipeline_v1
from fastapi import APIRouter, Request
from api.authentication.jwt_func import verify_token


# 子路由
sub_router = APIRouter()


@sub_router.post("/hello_world", summary="简单的函数调用", description='简单的函数调用')
async def port_hello_world(args: args.Args1, request: Request, token: bool = Depends(verify_token)): # token: bool = Depends(verify_token) 如果要加token
    client_host = f"{request.client.host}:{request.client.port}"   # 请求地址 port:host
    logger.info(f'host:{client_host} 请求: args{args}')
    ret = pipeline_v1(args, client_host)
    return ret
