# aocpo项目部署

## 一、拉取镜像

### 1.AI预测服务镜像

```shell
docker pull registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_predictor:1.0.0
```

~~~shell
docker pull registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_predictor_server:1.0.0
~~~

### 2.爬虫镜像
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_scrapyd:1.0.0
```
### 3.redis数据库镜像
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_redis:1.0.0
```
### 4.mongo数据库镜像
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_mongodb:1.0.0
```
### 5.aocpo系统镜像
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo:1.0.0
```
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_backend:1.0.0
```
### 6.Middleman模块镜像
```shell
docker pull registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_middleman:1.0.0
```
## 二、自定义网络
```shell
docker network creat -d bridge aocpo
```
## 三、创建容器

### 1.AI预测服务

```shell
docker run --name aocpo_predictor --network aocpo -d registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_predictor:1.0.0
```

```shell
docker run --name aocpo_predictor_server --network aocpo -d registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_predictor_server:1.0.0
```

### 2.爬虫

```shell
docker run --name aocpo_scrapyd --network aocpo -d registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_scrapyd:1.0.0
```

### 3.redis数据库

```shell
docker run --name aocpo_redis --network aocpo -v /var/redis_data:/data -d registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_redis:1.0.0
```

### 4.mongo数据库

```shell
docker run --name aocpo_mongodb --network aocpo -v /var/mongo_data/db:/data/db -v \
/var/mongo_data/configdb:/data/configdb -v /mongo_test:/mongo_test -d registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_mongodb:1.0.0
```

```shell
docker exec -it aocpo_mongodb mongorestore -d schoolData ~/schoolData
```

### 5.aocpo系统

```shell
docker run --name aocpo_backend --network aocpo -d registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_backend:1.0.0
```
```shell
docker run --name aocpo --network aocpo -p 80:80 -d registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo:1.0.0
```

### 6.Middleman

```shell
docker run --name aocpo_middleman --network aocpo -d registry.cn-hangzhou.aliyuncs.com/coderchen01/aocpo_middleman:1.0.0
```

### 7.查看容器运行状况

```shell
docker ps -a
```

如果出现如下结果则说明容器正常运行：

![运行结果](C:\Users\17322\AppData\Roaming\Typora\typora-user-images\1586183634066.png)

### 8.修改hosts文件

由于处于测试环境，需要修改客户端本地hosts文件。

windows平台：

1. 进入C:\Windows\System32\drivers\etc
2. 编辑hosts文件
3. 增加行 ip www.aocpo.com 如： 127.0.0.1 www.aocpo.com
域名不可更换。因为客户端通过此域名找到系统后端。


### 四、特别说明

新部署的系统，没有测试数据，需要新建任务，调用爬虫爬取数据。如需测试数据，可点击通过该[分享链接,提取码：exkb](https://pan.baidu.com/s/1FSe5In5k5U2Shn7NycUgOA )_，[备用链接](https://www.lanzous.com/ib29e5g) 下载测试数据。分别进行如下操作：

1. 将tiebaData，users文件夹上传到服务器根目录的mongo_test文件下

2. 执行如下命令：

```shell
docker exec -it aocpo_mongodb mongorestore -d tiebaData /mongo_test/tiebaData
```

```shell
docker exec -it aocpo_mongodb mongorestore -d users /mongo_test/users
```

  3.最后可进入系统登录测试账号：18175006085 密码：10191019
