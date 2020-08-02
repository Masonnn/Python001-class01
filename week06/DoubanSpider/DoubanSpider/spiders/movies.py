# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from DoubanSpider.items import DoubanspiderItem
from selenium import webdriver
import time


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movie.douban.com']

    # start_urls = ['http://movie.douban.com/']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=0'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        item = DoubanspiderItem()

        for movie in movies:
            film_name = movie.xpath('./div[1]/span/text()').extract()

            film_genre = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
            play_date = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip()
            item['film_name'] = film_name
            item['play_date'] = play_date
            item['film_genre'] = film_genre

            yield item
