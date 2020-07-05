# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Wk2Hw1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    film_name = scrapy.Field()
    film_genre = scrapy.Field()
    play_date = scrapy.Field()
