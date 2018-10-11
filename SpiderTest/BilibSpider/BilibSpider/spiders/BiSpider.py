# -*- coding: utf-8 -*-
import scrapy
import json
from BilibSpider.items import  BilibspiderItem
# 成功怕取billi的图片(可以使用)
class BispiderSpider(scrapy.Spider):
    name = "BiSpider"
    # allowed_domains = ["app.bilibili.com"]
    start_urls = ('https://app.bilibili.com/x/feed/index?build=5290000',)
    count = 0

    def parse(self, response):

        item = BilibspiderItem()
        bili_json = json.loads((response.text).encode('utf-8'))
        for content in bili_json['data']:
            item['title'] = content.get('title', '')
            item['image'] = content.get('cover', '')
            yield item
            print('*'*30)
        self.count+=1
        yield  scrapy.Request('https://app.bilibili.com/x/feed/index?build=529000'+str(self.count),callback=self.parse)

