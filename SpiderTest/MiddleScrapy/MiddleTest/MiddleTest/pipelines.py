# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
class MiddletestPipeline(object):
    # def __init__(self):
    #     self.big_a =

    def process_item(self, item, spider):
        items = dict(item)
        self.big_dir ='/home/python/Desktop/con/'+items['big_title']
        if not os.path.exists('/home/python/Desktop/con/'+items['big_title']):
            os.mkdir('/home/python/Desktop/con/'+items['big_title'])
        for count in items['small_title']:
            if not os.path.exists('/home/python/Desktop/con/' + items['big_title']+'/'+count):
                os.mkdir('/home/python/Desktop/con/' + items['big_title']+'/'+count)
        for my_url in items['small_a']:
            response = scrapy.Request(my_url)
            with open(self.big_dir+item['small_'][])
            # with open(my_url[-5],w)as f:
            #     f.write()

        return item

    # def deal_content(self, response):
    #
    #     with
