# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     v1_encapsulation
   Description :  用于封装调用函数
   Author :       jpl
   date：          2021/8/16
-------------------------------------------------
   Change Activity:
                   2021/8/16:
-------------------------------------------------
"""
__author__ = 'Asdil'
import uuid
import random
import asyncio
from common import *
from core import conf
from fastapi import APIRouter, Request
from schemas.response import response_code
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore



# 子路由2
scheduler_router = APIRouter()
Schedule = None


# @scheduler_router.on_event("startup")
# async def set_schedule_avaliable():
#     """配合load_schedule_or_create_blank使用, 初始化start_up表可用"""
#     sleep = random.uniform(0, 1)
#     await asyncio.sleep(sleep)



@scheduler_router.on_event("startup")
async def load_schedule_or_create_blank():
    """
    方法用于在项目启动时运行定时任务模块
    """
    sleep = random.uniform(1, 3)
    await asyncio.sleep(sleep)
    flag = sqlite3_db.select_one(conf.SQL_ITE2)[0]
    if flag == 1:
        sqlite3_db.excute(conf.SQL_ITE3)
    else:
        return

    # 定时任务, 加载定时任务模块, 一分钟监听一次kafka
    global Schedule
    try:
        jobstores = {'default': SQLAlchemyJobStore(url=f'sqlite:///{conf.TEMP_DB}')}
        Schedule = AsyncIOScheduler(jobstores=jobstores)
        Schedule.start()
        logger.info("定时任务模块启动！")
    except:
        logger.error("错误！不能加载定时任务模块！")


# @sub_router2.post("/set_schedule_job", summary="用于开启定时任务", description='用于开启定时任务', tags=["SCHEDULER"])
# def set_cpu_scanner_job(args: args.Args_None, request: Request):
#     random_suffix = uuid.uuid1()
#     job_id = str(random_suffix)
#     job = Schedule.add_job('这里填写任务函数', 'interval', seconds=5, id=job_id, args=[job_id])
#     job_id = job.id
#     logger.info(f"开启定时任务: id = {job_id}")
#
#     return response_code.resp_200(data={"job_id": job_id})

@scheduler_router.post("/del_schedule_job", summary="删除指定定时任务", description='删除指定定时任务', tags=["SCHEDULER"])
def del_cpu_scanner_job(args: args.Args_Del, request: Request):
    client_host = f"{request.client.host}:{request.client.port}"  # 请求地址 port:host
    logger.info(f'host:{client_host} 请求: args{args}')
    Schedule.remove_job(args.job_id)
    logger.info(f"删除定时任务: id = {args.job_id}")

    return response_code.resp_200(data={"job_id": args.job_id})


@scheduler_router.on_event("shutdown")
async def pickle_schedule():
    """
    方法用于在项目结束时关闭定时任务模块
    """
    sqlite3_db.excute(conf.SQL_ITE1)  # 初始化可开工任务
    global Schedule
    Schedule.shutdown()
    logger.info("关闭定时任务模块！")
