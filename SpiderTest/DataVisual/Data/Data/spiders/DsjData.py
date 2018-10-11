# -*- coding: utf-8 -*-
# import scrapy
# import time
# import datetime
# import json
# from Data.items import DataItem
#
# class DsjdataSpider(scrapy.Spider):
#     name = "DsjData"
#     date = datetime.datetime.strptime("2016-8-24", "%Y-%m-%d")
#     url ="http://data.guduomedia.com/show/datalist?category=NETWORK_VARIETY&t=1535365009632&date="
#     # allowed_domains = ["www.baidu.com"]
#     start_urls = []
#     print(time.strftime('%Y.%m.%d',time.localtime(time.time())))
#     while True:
#
#         if str(time.strftime('%Y-%m-%d',time.localtime(time.time()))) == str(date).split()[0]:
#             break
#         # time.sleep(1)
#         start_urls.append(url + str(date).split()[0])
#         date += datetime.timedelta(days=1)
#         for i in start_urls:
#             print(i)
#
#
#
#
#     def parse(self, response):
#         item = DataItem()
#         dd = json.loads(response.text)
#         print(dd)
#         for i in range(10):
#             count = dd['data']['totalBillboardList'][i]['total_play_count'].encode('utf-8')
#
#             if count.find('亿')>0 and count.find('万')>0:
#                 temp = str(int(count[:count.find('亿')])*100000000)
#                 temp2 = str(int(count[count.find('亿')+3:count.find('万')])*10000)
#                 count = str(int(temp2)+int(temp))
#                 # count =int(temp)+int(temp2)
#             elif count.find('万') > 0:
#                 count = str(int(count[:count.find('万')+3]) * 10000)
#             # if count.find('万'):
#             #     count = str(int(count[:count.find('万')]) * 10000)
#             item['value'] = count
#             item['name'] = dd['data']['totalBillboardList'][i]['name'].encode('gbk')
#             item['date'] = response.url[response.url.rfind('=')+1:]
#             yield item