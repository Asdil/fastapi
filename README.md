## fastapi模板

简易的fastapi模板

### 1.函数编写
函数在/api/文件夹下编写，一个项目新建一个子文件夹，代码放在子文件夹下面，主函数入口为pipline函数 
```
比如事例主函数入口为
/api/v1/func/hello_world.py 中的pipeline函数

/api/v1/v1_encapsulation.py 用来封装post/get 地址
```

### 2.路由编辑
将/api/v1/v1_encapsulation.py 文件中的hello_world函数注册到，/router/v1_router.py中，详见具体文件

### 3.部署
bash build.sh 容器名称 端口 文件夹地址

### 4.文档
文档路径在　host:port/docs路径下面