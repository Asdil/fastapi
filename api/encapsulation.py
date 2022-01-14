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
from common import *
from core import conf
from api import pipeline_v1
from fastapi import APIRouter, Request
from schemas.response import response_code
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


# 子路由
sub_router = APIRouter()
Schedule = None


@sub_router.on_event("startup")
async def load_schedule_or_create_blank():
    """
    方法用于在项目启动时运行定时任务模块
    """
    global Schedule
    try:
        jobstores = {
            'default': SQLAlchemyJobStore(url=f'sqlite:///{conf.TEMP_DB}')
        }
        Schedule = AsyncIOScheduler(jobstores=jobstores)
        Schedule.start()
        logger.info("定时任务模块启动！")
    except:
        logger.error("错误！不能加载定时任务模块！")


@sub_router.on_event("shutdown")
async def pickle_schedule():
    """
    方法用于在项目结束时关闭定时任务模块
    """
    global Schedule
    Schedule.shutdown()
    logger.info("关闭定时任务模块！")


# @sub_router.post("/set_schedule_job/", summary="用于开启定时任务", description='用于开启定时任务', tags=["API"])
# def set_cpu_scanner_job():
#     random_suffix = uuid.uuid1()
#     job_id = str(random_suffix)
#     job = Schedule.add_job(函数名称, 'interval', seconds=30, id=job_id, args=[job_id])
#    # job_id = Schedule.add_job(set_today, 'cron', day_of_week='*', hour='09', minute='15', id=args.uid, args=None)
#
#     job_id = job.id
#     logger.info(f"开启定时任务: id = {job_id}")
#
#     return response_code.resp_200(data={"job_id": job_id})

@sub_router.post("/del_schedule_job/", summary="删除指定定时任务", description='删除指定定时任务', tags=["API"])
def del_cpu_scanner_job(args:comm_args.Args_del_schedule, request: Request):
    client_host = f"{request.client.host}:{request.client.port}"  # 请求地址 port:host
    logger.info(f'host:{client_host} 请求: args{args}')

    Schedule.remove_job(args.job_id)

    logger.info(f"删除定时任务: id = {args.job_id}")

    return response_code.resp_200(data={"job_id": args.job_id})


@sub_router.post("/hello_world/", summary="简单的函数调用", description='简单的函数调用')
async def hello_world(args: v1_args.Args_v1, request: Request):
    client_host = f"{request.client.host}:{request.client.port}"   # 请求地址 port:host
    logger.info(f'host:{client_host} 请求: args{args}')
    ret = pipeline_v1(args, client_host)
    return ret
