#!/bin/bash
CONTER_NAME='xxx'                 # 容器名称
FILE_DIR='/python/code/fastapi'   # 文件地址
IMAGE='fastapi:v11'               # 镜像文件
MULTI_PROCESS=2                   # 线程数
IP='127.0.0.1'                    # 物理机IP
OUTER_PORT=1122                   # 物理机器端口
INNER_PORT=1122                   # 容器端口
docker run --name=$CONTER_NAME -p $IP:$OUTER_PORT:$INNER_PORT -v $FILE_DIR:/code -d -i -t $IMAGE \
bash /code/run.sh $INNER_PORT $MULTI_PROCESS