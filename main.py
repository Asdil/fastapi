# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
import uvicorn
from core.server import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8100, workers=3)
    # , reload=False, debug=False, workers=1, access_log=False