# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Id = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    handling = scrapy.Field()
    datime = scrapy.Field()
    content = scrapy.Field()

