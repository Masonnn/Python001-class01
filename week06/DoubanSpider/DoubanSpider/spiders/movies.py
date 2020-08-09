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
        # url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=0'
        url = 'https://movie.douban.com/subject/30464908/?tag=%E7%83%AD%E9%97%A8&from=gaia'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        item = DoubanspiderItem()

        for movie in movies:
            film_name = movie.xpath('./div[1]/span/text()').extract()

            film_stars = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
            film_shorts = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip()
            item['film_name'] = film_name
            item['film_stars'] = film_stars
            item['film_shorts'] = film_shorts

            yield item
