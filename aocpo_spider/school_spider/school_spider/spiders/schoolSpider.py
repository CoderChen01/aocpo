# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import SchoolSpiderItem


class SchoolSpider(scrapy.Spider):
    name = 'schoolSpider'
    allowed_domains = ['school.nihaowang.com']
    start_urls = ['http://school.nihaowang.com/']
    base_url = 'http://school.nihaowang.com/rank/6122/{page}.html'

    def start_requests(self):
        for page_num in range(1, 56):
            yield Request(url=self.base_url.format(page = str(page_num)), callback=self.parse)


    def parse(self, response):
        school_list = response.xpath("//li[@class='ranking_bg']")
        for school in school_list:
            _school = SchoolSpiderItem()
            data = list(map(lambda _: _.strip().replace('\r\n', ''), school.xpath(".//a/text()").extract()[:2]))
            _school['ranking'] = data[0]
            _school['school'] = data[1]

            yield _school

