# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     router
   Description :  用于注册路由
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
from core import conf
from fastapi import APIRouter
from api.encapsulation import sub_router

router = APIRouter()

# 添加定时任务模块
if conf.ADD_SCHEDULER:
    from api.scheduler import scheduler_router
    router.include_router(scheduler_router, tags=["定时任务服务"])

router.include_router(sub_router, tags=["接口服务"])
