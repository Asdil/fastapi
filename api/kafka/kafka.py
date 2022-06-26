# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       asdil
   date：          2022/2/25
-------------------------------------------------
   Change Activity:
                   2022/2/25:
-------------------------------------------------
"""
__author__ = 'Asdil'
# import json
# from core import conf
# from common import logger
# from common import sqlite3_db
# from aiokafka import AIOKafkaConsumer
#
#
# async def main():
#     """monitor方法用于监听kafka消息执行操作
#     """
#     logger.info('master kafka初始化...')
#     # kafka监听
#     consumer = AIOKafkaConsumer(conf.KAFKA_TOPIC,
#                                 bootstrap_servers=conf.KAFKA_HOSTS,
#                                 value_deserializer=lambda data: json.loads(data),
#                                 auto_offset_reset=conf.AUTO_OFFSET_RESET)
#     logger.info('kafka初始化完成！')
#     await consumer.start()
#     try:
#         # 获取kafka信息
#         logger.info('kafka开始监听...')
#         async for msg in consumer:
#             msg = msg.value
#             station = msg['station']
#             sql = f"insert into task(station) values ('{station}')"
#             sqlite3_db.excute(sql)
#             logger.info(f'kafka 获取消息{msg}, 写入数据库...')
#     finally:
#         # 最后停止程序
#         await consumer.stop()
#         logger.info('kafka关闭！')
#     return 0
#
#
# # 用法
# # @sub_router.on_event('startup')
# # async def start_kafka():
# #     asyncio.create_task(main())