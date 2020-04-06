# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urlencode
from scrapy.http import Request
import re
from ..items import postDataItem, authorDataItem

class BtspiderSpider(scrapy.Spider):
    name = 'tbSpider'
    allowed_domains = ['tieba.baidu.com']
    base_url = 'http://tieba.baidu.com'
    args = None #传入

    #爬虫构建Request对象
    def start_requests(self):
        """
        开始搜索相关学校贴吧
        """
        self.args = json.loads(self.args)
        search_base_url = 'http://tieba.baidu.com/f/search/fm?ie=UTF-8&'
        arg1 = urlencode({'qw':self.args.get('school', None)}) #通过命令行传递属性
        search_url = search_base_url + arg1
        yield Request(url=search_url, callback=self.get_search_page_urls, dont_filter=True) #搜索的url送到调度器， 注意：这个url不参与去重下面用到


    #开始搜索相关贴吧
    def get_search_page_urls(self, response):
        """
        获得搜索结果所有页面，
        发送每页的url到调度器
        """
        pager_search = response.xpath("//div[@class='pager pager-search']/a/@href").extract()[:-2]
        pager_search = [(self.base_url + pager) for pager in pager_search ]
        pager_search.append(response.url)
        for pager_url in pager_search:
            yield Request(url=pager_url, callback=self.get_forum_urls)

    #获得相关贴吧
    def get_forum_urls(self, response):
        """
        获得所有相关贴吧的url送到调度器
        """
        forum_lists = response.xpath('//div[@class="search-forum-list"]/div[@class="forum-item clear-float"]')
        for forum in forum_lists:
           forum_url = self.base_url + forum.xpath('./div[@class="left"]/a/@href').extract_first()
           yield Request(url=forum_url, callback=self.get_post_urls)

    #获得贴吧帖子
    def get_post_urls(self, response):
        """
        获得所有帖子的url
        """
        data_tid_list = re.findall("data-tid='(\d*?)'", response.text)
        for data_tid in data_tid_list:
            post_url = self.base_url + '/p/' + data_tid
            yield Request(url=post_url, callback=self.get_post_data)
        #实现翻页操作
        rhref = re.compile('<a href="(.*?)" class=" pagination-item " >')
        url_list = re.findall(rhref, response.text)
        for url in url_list:
            if int(re.findall('.*pn=(\d*)',url)[0]) <= int(self.args.get('scale', 1000)):
                yield response.follow(url=url, callback=self.get_post_urls)
            else:
                break

    #获得帖子内容
    def get_post_data(self, response):
        """
        获取一个帖子的数据，并做简单的清洗，并且将用户返回到get_user_info处理
        可能部分帖子有意外，直接忽略
       """
        # 提取帖子内容的正则表达式，来源为页面底部JavaScript代码
        rpost = '"firstPost": (?P<data>\{"title":(null|".*"),"content":(null|".*"),"is_vote".*"now_time":\d*)'
        post = re.search(rpost, response.text)
        if post:
            post_data_item = postDataItem()

            post_data = json.loads(post.group('data') + '}')

            post_data_item['school'] = self.args.get('school', None)
            # 提取帖子id
            tid = re.compile("https?://tieba.baidu.com/p/(\d*).*").findall(response.url)[0]
            post_data_item['tid'] = tid

            # 找到所有标签替换为空
            post_data_item_title = re.sub('(&nbsp;|<.*?>)', '', str(post_data.get('title')))\
                .replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').strip()
            post_data_item['title'] = re.sub('&#.*?;', '', post_data_item_title)
            post_data_item_content = re.sub('(&nbsp;|<.*?>)', '', str(post_data.get('content')))\
                .replace('&quot;', '"').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').strip()
            post_data_item['content'] = re.sub('&#.*?;', '', post_data_item_content)

            # 时间戳
            post_data_item['date'] = post_data.get('now_time')

            # 提取作者的xpath表达式
            xauthor = "//div[contains(@class, 'louzhubiaoshi')]/@author"
            post_data_item['author_name'] = response.xpath(xauthor).extract_first()

            # 提取楼层回复内容的xpath表达式,是所有的内容
            # 这是经过清洗的数据用它来做分析
            xreply_content = "//div[contains(@class, 'd_post_content')]/text()"
            all_content = response.xpath(xreply_content).extract()
            all_content_dirty = ''.join(all_content)
            post_data_item['reply_content'] = ''.join(re.findall(r'[\u4e00-\u9fa5]', all_content_dirty))

            # 提取帖子回复数量的xpath表达式
            xreply_num = "//span[@class='red']/text()"
            num_str = response.xpath(xreply_num).extract_first()
            if '万' in num_str:
                num = int(float(num_str.replace('万', '')) * 10000)
            else:
                num = int(num_str)
            post_data_item['reply_num'] = num

            #提取设备的xpath表达式
            xdevice = "//div[contains(@class, 'l_post')]/@data-field"
            device_dirty = ''.join(response.xpath(xdevice).extract())
            post_data_item['device'] = list(filter(lambda _: _ != '', re.findall('"open_type":"([aplendroi]*)"', device_dirty))) #去除空值，转换列表
            yield post_data_item

            author_url = "http://tieba.baidu.com/home/get/panel?ie=utf-8&un=%s" % (post_data_item['author_name'])
            yield Request(url=author_url, callback=self.get_user_info)

    #获取用户信息
    def get_user_info(self, response):
        """
        获得用户信息
        """
        user_info = authorDataItem()
        info = json.loads(response.text)
        if info.get('error') == '成功':
            info_data = info.get('data')
            user_info['school'] = self.args.get('school', None)
            user_info['user_name'] = info_data.get('name')
            user_info['name_show'] =info_data.get('name_show')
            user_info['sex'] = info_data.get('sex')
            user_info['tb_age'] = float(info_data.get('tb_age'))
            post_num = info_data.get('post_num')
            if isinstance(post_num,str):
                post_num = int(float(post_num.replace('万', '').strip()) * 10000)
            user_info['post_num'] = int(post_num)
            user_info['tb_vip'] = info_data.get('tb_vip')
            fans = info_data.get('followed_count')
            if isinstance(fans, str):
                fans = int(float(fans.replace('万', '').strip()) * 10000)
            user_info['fans'] = int(fans)
            return user_info
        else:
            return None
