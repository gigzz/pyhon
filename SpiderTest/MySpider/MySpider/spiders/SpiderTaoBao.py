# encoding:utf8
import scrapy
from MySpider.items import MyspiderItem
# 爬取斗鱼(成功)
class TaoBaoSpider(scrapy.Spider):
    name = 'TaoBao'
    allowed_domains = ['https://www.baidu.com']
    start_urls = ['https://www.douyu.com/directory/all']

    def parse(self, response):
        zibos = response.xpath("//ul[contains(@id, 'live-list-contentbox')]/li")
        # print(len(zibos)).
        # dy_data = []
        for i in zibos:
            item = MyspiderItem()
            dy_title = i.xpath("./a/div//h3/text()")[0].extract().strip()
            # print(dy_title)
            dy_type = i.xpath("./a/div//span[@class='tag ellipsis']/text()")[0].extract()
            # print(dy_type)
            dy_name = i.xpath("./a/div//p/span[@class='dy-name ellipsis fl']/text()")[0].extract()
            # print(dy_name)
            dy_count = i.xpath("./a/div//p/span[@class='dy-num fr']/text()")[0].extract()
            item['name'] = dy_name.encode('utf-8')
            item['title'] = dy_title
            item['type_video'] = dy_type.encode('utf-8')
            item['count'] = dy_count.encode('utf-8')
            # 使用yield吧每一个item返回给管道处理
            yield item
            # print(item)
            # item['name'] = dy_name.encode('gbk')
            # item['title'] = (dy_title).encode('utf-8')
            # item['type_video'] = dy_type.encode('gbk')
            # item['count'] = dy_count.encode('gbk')
            # dy_data.append(item)
        # return dy_data
            # 保存-o xxx.json  或-o csv
            # print(dy_count)
        # with open('ss.txt','w') as f:
        #     f.write(response.body)