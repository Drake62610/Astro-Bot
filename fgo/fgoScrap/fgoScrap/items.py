# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ServantItem(scrapy.Item):
    name = scrapy.Field()
    stars = scrapy.Field()
    sclass = scrapy.Field()
    image_url = scrapy.Field()

class EssenceItem(scrapy.Item):
    name = scrapy.Field()
    stars = scrapy.Field()
    image_url = scrapy.Field()