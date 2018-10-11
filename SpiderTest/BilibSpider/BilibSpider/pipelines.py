# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

# 继承ImagePipeline类来处理图片
class BilibspiderPipeline(ImagesPipeline):
    # #
    # def process_item(self, item, spider):
    #     # print(item)
    #     # print(item['image'])
    #     a = scrapy.Request(item['image']).body
    #     print('%r'%a)
    #     # with open(item['title']+'.jpg','wb')as f:
    #     #     f.writelines(a)
    #     return item
    #     # pass


# class MyImagesPipeline(ImagesPipeline):
#
#
    def get_media_requests(self, item, info):
        image_url = item['image']
        print(image_url)
        yield scrapy.Request(image_url, dont_filter=True)

    def item_completed(self, results, item, info):
        # image_path = [x['path'] for ok, x in results if ok]
        # if not image_path:
        #     item['image_paths'] = image_path
        print('进入')
        print(results)
        return item
