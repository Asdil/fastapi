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
from fastapi import APIRouter
from api.encapsulation import sub_router
router = APIRouter()

router.include_router(sub_router, tags=["hello world 接口"])