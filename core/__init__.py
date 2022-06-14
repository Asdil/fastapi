# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :  配置文件区分生产和开发
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
# docker 生产环境下需要添加语句 --env DEBUG=false
# pycharm 需要在run->Edit Configuration->Environment->添加;DEBUG=true

import os
ENV = os.environ
if ENV.get('DEBUG', 'true') == 'false':
    from core.config import development_config as conf
else:
    from core.config import production_config as conf

