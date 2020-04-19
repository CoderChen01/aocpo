# aocpo
## Warning: 该运行方法较为繁琐，本项目已通过docker封装，可通过docker运行，[具体链接](https://github.com/CoderChen01/aocpo/blob/master/docker-run.md)

* 请安装python依赖利用文件夹里的requirements.txt，此外安装PaddlePaddle框架，因为AI模型基于它

* 请安装MongoDB，redis数据库，为了方便请不要设置密码等访问权限

* 更改源码中的各个url

* 更改MongoDB,redis的url：
    aocpo_backend > aocpo > settings > MONGO_URL and REDIS_URL #项目后端
    tbSpider_primary > tbSpider > settings > MONGO_URL and REDIS_URL #用于抓取百度贴吧内容
    middleman_script > middleman > settings >  MONGO_URL and REDIS_URL #用于为爬虫分配任务
    school_spider > school_spider > settings > MONGO_URL #用于抓取中国高校校名及排名

* 运行school_spider抓取中国高校的校名及排名，后面用于新建任务输入框提示，增加用户体验
    scrapy crawl school_spider

* 利用scrapyd框架部署tbSpider_primary，记住scrapyd的ip + 端口(tbSpider_primary需要更改MongoDB,redis的url如下)

* 由于模型过大，无法发在git。百度网盘下载，放入爬虫预测API代码中对于文件中。地址：[提取码：vqlx](https://pan.baidu.com/s/1u_Z_6MNo53UtW3r1lbs-1A)

* 在linux中使用Nginx + uwsgi + supervisor部署aocpo_AI_models_api的django项目（用于预测，需要承受较大的并发，使用python自带web服务器会吃不消，故需要部署）

* 进入aocpo_frontend，安装依赖（vue开发的，需要安装node）

* windows中运行aocpo_backend

* 更改aocpo_frontend后端url（对应的就是上一步中其所在的ip + 端口）

* 运行aocpo_frontend

* 运行middleman_script
