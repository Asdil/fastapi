# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mock
   Description :
   Author :       fibrizoasdil
   date：          2022/8/15
-------------------------------------------------
   Change Activity:
                   2022/8/15:
-------------------------------------------------
"""
__author__ = 'Asdil'
from fastapi import APIRouter
from schemas.response import response_code

# 子路由
mock_router = APIRouter()


@mock_router.api_route("/mock/{url}", methods=["post", "get", "delete", "put"], include_in_schema=False)
async def mock(url: str):
    print(url)
    return response_code.resp_200_udf(**{"2": 2})
