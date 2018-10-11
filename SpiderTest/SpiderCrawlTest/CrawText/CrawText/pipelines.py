# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
class CrawtextPipeline(object):
    def process_item(self, item, spider):
        texts = json.dumps(dict(item), ensure_ascii=False)+'\r\n\r\n'
        with open('数据.txt', 'a')as f:
            f.write(texts.encode('utf-8'))
        # print(texts.encode('utf-8'))
        return item
