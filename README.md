# docker fastapi 部署


# 1. fastapi程序
⛳ ♠️ ♥️ ♣️ ♦️ ☕

### 1.1 新建接口

- #### 1.1.1 定义参数：
       项目文件夹->common->args->args.py文件
	   添加参数文件
	   


- ```
from pydantic import BaseModel
from typing import Union, Optional
class Args1(BaseModel):
    """
    ArgsL1 类用于
    """
    l1: str                # 定义l1为字符型
	l2: Optional[int, str] # 定义l2可以是字符也可以是整型
	l3: str = None         # 定以默认值为空
	

- #### 1.1.2 编写函数：
	   项目文件夹->api->新建或者已有的文件夹->xxx.py文件
	   
	   
	 

- ```
def hello_world(args, host):
	args为1.1.1的参数对象
	host为请求地址，用于log日志用，这个可以不要
	
	args调用方式为args.l1, args.l2
	args可以转换为字典 dict(args)

- #### 1.1.3 定义接口：
       项目文件夹->ap->encapsulation.py

- ```
@sub_router.post("/hello_world", summary="简单的函数调用", description='简单的函数调用')
async def port_hello_world(args: args.Args1, request: Request):
    client_host = f"{request.client.host}:{request.client.port}"   # 请求地址 port:host
    logger.info(f'host:{client_host} 请求: args{args}')
    ret = hello_world(args, client_host)
    return ret
sub_router                      为路由对象
/hello_world                    为接口地址
args: args.Args1                表示args参数对象是args.Args1
request: Request                表示获取请求对象的信息
client_host                     获取请求对象的ip
port_hello_world                这个是接口函数，注意不要和其他对象或者函数重名
hello_world(args, client_host)  表示调用hello_world函数
```

### 1.2 定时任务
   加载定时任务需  项目文件夹->core->common_config.py->ADD_SCHEDULER = True

- #### 1.2.1 编写定时任务函数

- ```
	def task(job_id):
		定时任务的第一个参数一定是job_id, 其他参数写在后面


- #### 1.2.2 启动定时任务模块
- ```
	项目文件夹->api->scheduler.py
	
	@scheduler_router.on_event("startup")
	async def load_schedule_or_create_blank():
	该函数是启动定时任务模块的函数, 由于多进程情况下定时任务模块可能加载多次，所里函数里面会有一个锁，保证每次只加载一次定时任务模块

- #### 1.2.3 启动定时任务
- ```
@scheduler_router.post("/set_schedule_job", summary="用于开启定时任务", description='用于开启定时任务', tags=["SCHEDULER"])
async def set_cpu_scanner_job(args: args.Args_none, request: Request):
    random_suffix = uuid.uuid1()
    job_id = str(random_suffix) # 43200
    job = Schedule.add_job(paving.main, 'interval', seconds=5, id=job_id, args=[job_id])
    job_id = job.id
    logger.info(f"开启定时任务: id = {job_id}")
    return response_code.resp_200(data={"job_id": job_id})
	
	该函数用来启动定时任务
	Schedule.add_job 表示设置定时任务
	这里设置为循环模式每5秒触发一次
	
	函数定义好之后需要post一下这个接口，然后程序就会把定时任务再加到数据库，开始运行定时任务


- #### 1.2.4 关闭定时任务
- ```
	@scheduler_router.post("/del_schedule_job", summary="删除指定定时任务", description='删除指定定时任务', tags=["SCHEDULER"])
	async def del_cpu_scanner_job(args: args.Args2, request: Request):
    	client_host = f"{request.client.host}:{request.client.port}"  # 请求地址 port:host
    	logger.info(f'host:{client_host} 请求: args{args}')
    	Schedule.remove_job(args.job_id)
    	logger.info(f"删除定时任务: id = {args.job_id}")
    	return response_code.resp_200(data={"job_id": args.job_id})
		
		args.job_id 表示某个定时任务的job_id
		
### 1.3 kafka任务
		项目文件夹->api->kafka->kafka.py
		需要配置kafka


### 1.4 docker启动任务
	docker run --name=容器名称 -p 主机ip:主机接口:容器接口  -v 程序文件夹:/code -d -i -t 镜像名称:镜像版本 /root/miniconda3/bin/gunicorn --chdir /code main:app -b 0.0.0.0:主机接口 -w 进程数目 -k uvicorn.workers.UvicornWorker --reload
	
	example：
	docker run --name=pave -p 172.16.23.130:5654:5654  -v /raid/jiapeiling/code/paving:/code -d -i -t debain_fastapi:v6 /root/miniconda3/bin/gunicorn --chdir /code main:app -b 0.0.0.0:5654 -w 2 -k uvicorn.workers.UvicornWorker --reload
	
	我的脚本已经集合了所有参数 项目文件夹->start.sh 需要先修改参数再 bash start.sh
