# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CrawText.items import CrawtextItem
# 爬去东莞(成功)
class MycrawlSpider(CrawlSpider):
    name = 'MyCrawl'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']
    # start_urls = ['https://www.baidu.com/s?wd=504']
    # LinkExtractor(allow='写正则表达式',)
    rules = (
        # 如果不写毁掉函数的话会交给_parse_responsec处理也就相当于给parse处理
        Rule(LinkExtractor(allow=r'page=\d+')),
        Rule(LinkExtractor(allow=r'/2\d+/\d+'), callback= 'parse_item', follow=True)
    )

    def parse_item(self, response):
        item = CrawtextItem()
        a = response.xpath("//div[@class='pagecenter p3']/div/div/div[@class='cleft']/strong/text()").extract()
        # d = a[0].split()[0].split(':')[0].encode('utf-8')
        # print(d)
        item['title'] = a[0].split()[0].split(':')[0]
        item['number'] = a[0].split()[1].split(':')[1]
        item['state'] = response.xpath("//div[@class='audit']/div[@class='cleft']/span/text()").extract()[0]
        item['context'] = ('\n'.join(response.xpath("//div[@class='c1 text14_2']/text()|//div[@class='c1 text14_2']/div[@class='contentext']/text()")
                                    .extract()).replace('\n', '').replace(" ","").replace('\t', ""))
        # ''.split()
        # c =  response.xpath("//div[@class='c1 text14_2']/text()").extract()
        # print('\n'.join(c))
        # print('*'*3)
        yield item
