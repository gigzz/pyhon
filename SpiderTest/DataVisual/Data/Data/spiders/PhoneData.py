#coding:utf-8
import scrapy
import time
import datetime
import json
from Data.items import DataItem


class PhonedataSpider(scrapy.Spider):
    name = "PhoneData"
    date = datetime.datetime.strptime("20151030", "%Y%m%d")
    url ="http://insight.baidu.com/base/search/rank/list?pageSize=15&dimensionid=37&dateType="
    # allowed_domains = ["www.baidu.com"]
    start_urls = []
    # print(time.strftime('%Y.%m.%d',time.localtime(time.time())))
    while True:
        print(date)
        if str(time.strftime('%Y-%m%-d',time.localtime(time.time()))) < str(date).split()[0]\
                or str(date+datetime.timedelta(days=1)) >= str(time.strftime('%Y-%m%-d',time.localtime(time.time()))):
            date = time.strftime('%Y%m%d',time.localtime(time.time()))
            start_urls.append(url + str(date).split()[0])
            break
        # time.sleep(1)
        start_urls.append(url + str(date.strftime('%Y%m%d')).split()[0])
        date += datetime.timedelta(days=1)
        # for i in start_urls:
            # print("*"*50)
            # print(i)




    def parse(self, response):
        item = DataItem()
        dd = json.loads(response.text)
        # print(dd)
        for i in range(15):
            count = dd['data']['results']['current'][i]['value'].encode('utf-8')

            if count.find('亿')>0 and count.find('万')>0:
                temp = str(int(count[:count.find('亿')])*100000000)
                temp2 = str(int(count[count.find('亿')+3:count.find('万')])*10000)
                count = str(int(temp2)+int(temp))
                # count =int(temp)+int(temp2)
            elif count.find('万') > 0:
                count = str(int(count[:count.find('万')]) * 10000)
            # if count.find('万'):
            #     count = str(int(count[:count.find('万')]) * 10000)
            item['value'] = count
            item['name'] = dd['data']['results']['current'][i]['item'].encode('gbk')
            item['date'] = dd['data']['results']['currDate']
            # print(count)
            # print(item.get('name'))
            # print(item.get('date'))
            yield item
