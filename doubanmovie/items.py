# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    region = scrapy.Field()
    category = scrapy.Field()
    rate = scrapy.Field()
    score_number = scrapy.Field()
    comment = scrapy.Field()

