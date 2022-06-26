# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     server
   Description :
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'

import traceback
from core import conf
from router.router import router
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware
from schemas.response.response_code import UnicornException


def create_app() -> FastAPI:
    """
    create_app方法用于生成FatAPI对象
    """
    app = FastAPI(
        debug=conf.DEBUG,
        title=conf.TITLE,
        description=conf.DESCRIPTION,
    )
    app.mount('/static', StaticFiles(directory='static'),
              name='static')
    '''
    docs修改方法
    1. vim Lib/site-package/fastapi/openapi/docs.py
    2. 替换
    swagger_js_url: str="/static/swagger-ui/swagger-ui-bundle.js",
    swagger_css_url: str="/static/swagger-ui/swagger-ui.css",
    swagger_favicon_url: str="/static/swagger-ui/favicon.png",
    
    redoc_js_url: str = "/static/redoc/bundles/redoc.standalone.js",
    redoc_favicon_url: str = "/static/redoc/favicon.png",
    打开http://127.0.0.1:端口/docs就可以成功加载
    '''

    # 其余的一些全局配置可以写在这里 多了可以考虑拆分到其他文件夹

    # 跨域设置
    register_cors(app)

    # 注册路由
    register_router(app)

    # 注册捕获全局异常
    register_exception(app)

    return app


def register_router(app: FastAPI) -> None:
    """
    register_router方法用于注册路由
    """
    # 项目API
    app.include_router(
        router,
    )


def register_cors(app: FastAPI) -> None:
    """
    register_cors方法用于跨域设置
    """
    if conf.DEBUG:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_exception(app: FastAPI) -> None:
    """
    register_cors方法用于跨域设置
    """
    @app.exception_handler(UnicornException)
    async def unicorn_exception_handler(request: Request, exc: UnicornException):
        return JSONResponse(
            status_code=exc.code,
            content={
                "code": exc.code,
                # "data": None,
                "message": exc.message,
            },
        )

