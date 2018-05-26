# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()


class DanKangItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    subtitle = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()

class ConfluenceItem(scrapy.Item):
    pageId = scrapy.Field()
    pageTitle = scrapy.Field()
    content = scrapy.Field()
    labels = scrapy.Field()



class TryingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
