# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     authority
   Description :
   Author :       asdil
   date：          2022/6/16
-------------------------------------------------
   Change Activity:
                   2022/6/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
from fastapi import Depends
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from api.authentication.jwt_func import login_for_access_token



# 子路由
authority_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@authority_router.post("/token", summary="获取Token", description='获取Token')
async def port_login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    ret = await login_for_access_token(form_data)
    return ret


