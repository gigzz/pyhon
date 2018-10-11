# -*- coding: utf-8 -*-
import scrapy
from MiddleTest.items import MiddletestItem
from MiddleTest.smallitem import SmallItem
class MiddlepSpider(scrapy.Spider):
    name = "MiddleP"
    # allowed_domains = ["www.baidu.com"]
    start_urls = (
        'https://www.sina.com.cn/',
    )
    item = MiddletestItem()
    def parse(self, response):

        all = response.xpath("//div[@class='main-nav']")[0]
        # for a in all.xpath('./div'):
            # for i in range(1,4):
        for b in all.xpath('./div/ul'):
            small = []
            small_a = []
            # if b.xpath('./li/a[1]/b/text()').extract():
            #     # print(b.xpath('./b/text()').extract())[0]
            #     item['big_title'] = b.xpath('./li/a/b/text()').extract()[0]
            # else:
                # for d in b.xpath('./text()'):
            for c in b.xpath('./li/a'):
                # print(len(b.xpath('./li/a')))
                if c.xpath('./b/text()').extract():
                    # print(b.xpath('./b/text()').extract())[0]
                    self.item['big_title'] = b.xpath('./li/a/b/text()').extract()[0]
                    self.item['big_a'] = b.xpath('./li/a/@href').extract()[0]
                else:
                    small_a.append(c.xpath('./@href').extract()[0])
                    small.append(c.xpath('./text()').extract()[0])
                # print(small)
            self.item['small_title'] = small
            self.item['small_a'] = small_a

            yield self.item
            # yield self.item
            # for new in small_a:
            #     yield scrapy.Request(new,callback=self.deal_a)

    # def deal_a(self, response):
    #     content = []
    #     # self.item['content'] =
    #     # response.xpath('')
    #     print(response.text)



