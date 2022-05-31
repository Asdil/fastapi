#!/bin/bash
echo "初始化数据表"
/miniconda3/bin/python /code/recover.py
echo "启动程序"
/miniconda3/bin/gunicorn --chdir /code main:app -b 0.0.0.0:$1 -w $2 -k uvicorn.workers.UvicornWorker --reload