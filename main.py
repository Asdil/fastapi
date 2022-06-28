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
import subprocess
from core.server import create_app

app = create_app()

if __name__ == '__main__':
    subprocess.check_call('python recover.py', shell=True)
    uvicorn.run('main:app', host='0.0.0.0', port=8100, workers=1)

# python recover.py && gunicorn main:app -b 0.0.0.0:8100 -w 4 -k uvicorn.workers.UvicornWorker --reload
