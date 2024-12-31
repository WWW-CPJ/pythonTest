# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DpcqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = scrapy.Field()
    author = scrapy.Field()
    status = scrapy.Field()
    date = scrapy.Field()
    # info = scrapy.Field()
    intro = scrapy.Field()
    # chapter = scrapy.Field()

class ChapterItem(scrapy.Item):
    chapter = scrapy.Field()
    


