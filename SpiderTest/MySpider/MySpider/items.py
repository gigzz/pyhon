# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    type_video = scrapy.Field()
    count = scrapy.Field()
