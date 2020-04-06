# -*- coding: utf-8 -*-

BOT_NAME = 'tbSpider'
SPIDER_MODULES = ['tbSpider.spiders']
NEWSPIDER_MODULE = 'tbSpider.spiders'
#配置日志输出等级
LOG_LEVEL = 'ERROR'
#你懂得
ROBOTSTXT_OBEY = False
#激活自定义下载中间件
DOWNLOADER_MIDDLEWARES = {
    'tbSpider.EmulateDownloaderMiddleware.Emulate': 543,
}
#激活piplines
ITEM_PIPELINES = {
    'tbSpider.pipelines.MongoPipeline': 300,
}
#并发数
CONCURRENT_REQUESTS = 50
#mongo的连接
MONGO_URI = 'mongodb://192.168.68.128:27017'
MONGO_DATABASE = 'tiebaData'

#####分布式设置#######
#更换调度器，去重组件
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
#redis连接配置
REDIS_URL = 'redis://192.168.68.128:6379'
#配置调度队列***不设置默认为优先级队列，这里默认
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
#配置持久化，默认为FALSE， 设置为TRUE后，爬取队列和去重指纹不会在爬取结束后自动清空，但是爬虫强制结束，是不会自动清空的
#SCHEDULER_PERSIST = False
#配置重爬， 强制中断爬虫会接着原来进度爬取，默认FALSE， 设置TRUE爬虫会重爬
# SCHEDULER_FLUSH_ON_START = True
#pipelines配置，scrapy_redis提供直接将item存储到redis的便捷，这里我们不选则
#ITEM_PIPELINES = {'scrapy_redis.piplines.RedisPIpeline':300,}

#预测api
PREDICTOR_URL = 'http://192.168.68.128:8080/AI_analysis?'







#SPIDER_MIDDLEWARES = {
#    'tbSpider.middlewares.TbspiderSpiderMiddleware': 543,
#}



# Configure maximum concurrent requests performed by Scrapy (default: 16)


# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html




# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
