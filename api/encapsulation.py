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
import uuid
from common import *
from core import conf
from api import pipeline_v1
from fastapi import APIRouter, Request
from schemas.response import response_code

# 子路由
sub_router = APIRouter()


@sub_router.post("/hello_world", summary="简单的函数调用", description='简单的函数调用')
async def hello_world(args: args.Args1, request: Request):
    client_host = f"{request.client.host}:{request.client.port}"   # 请求地址 port:host
    logger.info(f'host:{client_host} 请求: args{args}')
    ret = pipeline_v1(args, client_host)
    return ret
