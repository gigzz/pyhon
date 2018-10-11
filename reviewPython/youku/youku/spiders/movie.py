# -*- coding: utf-8 -*-
import scrapy

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        pass
