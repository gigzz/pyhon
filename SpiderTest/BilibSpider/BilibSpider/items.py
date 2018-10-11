# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibspiderItem(scrapy.Item):
    image = scrapy.Field()
    title = scrapy.Field()
