# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 爬取新浪新聞映射對象
class MiddletestItem(scrapy.Item):
    # 大標題
    big_title = scrapy.Field()
    big_a = scrapy.Field()

    # 小標題
    small_title = scrapy.Field()
    small_a = scrapy.Field()

    # 文章內容
    content = scrapy.Field()
    # 文章標題
    title = scrapy.Field()
    # 大標題位置
    dig_local = scrapy.Field()
    # 小標題位置dddDD
    small_local = scrapy.Field()
