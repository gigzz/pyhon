# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawtextItem(scrapy.Item):
    title = scrapy.Field()
    number = scrapy.Field()
    context = scrapy.Field()
    state = scrapy.Field()
