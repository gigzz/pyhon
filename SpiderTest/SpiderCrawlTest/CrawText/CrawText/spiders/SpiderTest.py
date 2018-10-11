# -*- coding: utf-8 -*-
import scrapy
from CrawText.items import CrawtextItem
# 使用spider完成(成功)
class SpidertestSpider(scrapy.Spider):
    name = "SpiderTest"
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']
    url_all = set()

    def parse(self, response):
        my_url = response.xpath("//div[@class ='pagination']/a/@href").extract()
        con_urls = response.xpath("//a[@class='news14']/@href").extract()
        print(con_urls)
        for url in my_url:
            pass
            yield scrapy.Request(url, callback=self.parse)
        for con_url in con_urls:
            yield scrapy.Request(con_url, callback=self.deal_cont)

    # def deal_url(self,response):
    #     print(response.text)
    #     return

    def deal_cont(self, response):
        item = CrawtextItem()
        a = response.xpath("//div[@class='pagecenter p3']/div/div/div[@class='cleft']/strong/text()").extract()
        # d = a[0].split()[0].split(':')[0].encode('utf-8')
        # print(d)
        item['title'] = a[0].split()[0].split(':')[0]
        item['number'] = a[0].split()[1].split(':')[1]
        item['state'] = response.xpath("//div[@class='audit']/div[@class='cleft']/span/text()").extract()[0]
        item['context'] = ('\n'.join(response.xpath(
            "//div[@class='c1 text14_2']/text()|//div[@class='c1 text14_2']/div[@class='contentext']/text()")
                                     .extract()).replace('\n', '').replace(" ", "").replace('\t', ""))
        # ''.split()
        # c =  response.xpath("//div[@class='c1 text14_2']/text()").extract()
        # print('\n'.join(c))
        # print('*'*3)
        yield item


