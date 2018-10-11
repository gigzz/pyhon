# -*- coding: utf-8 -*-
import scrapy

class Mylogin2Spider(scrapy.Spider):

    name = "MyLogin2"
    allowed_domains = ["www.baidu.com"]
    start_urls = (
        'http://www.www.baidu.com/',
    )

    def parse(self, response):
        pass
