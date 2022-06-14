#!/bin/bash
CONTER_NAME='tooling'                 # 容器名称
FILE_DIR='/home/jpl/tooling/tooling_digitalization'   # 文件地址
IMAGE='debain_fastapi:v4'               # 镜像文件
MULTI_PROCESS=2                   # 线程数
IP='0.0.0.0'                    # 物理机IP
OUTER_PORT=12002                   # 物理机器端口
INNER_PORT=12002                   # 容器端口
docker run --name=$CONTER_NAME --env DEBUG=false -p $IP:$OUTER_PORT:$INNER_PORT -v $FILE_DIR:/code -d -i -t $IMAGE \
bash /code/run.sh $INNER_PORT $MULTI_PROCESS