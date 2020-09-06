# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from Spiders.items import SpidersItem
import time


class SodasSpider(scrapy.Spider):
    name = 'sodas'
    allowed_domains = ['smzdm.com']

    def start_requests(self):
        url = 'https://www.smzdm.com/fenlei/qipaoshui/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.findAll('h5', attrs={'class': 'feed-block-title'})

        for title in title_list:
            item = SpidersItem()
            prd_name = title.find('a').get_text()
            link = title.find('a').get('href')
            item['prd_name'] = prd_name
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    # 解析评论页面
    def parse2(self, response):
        item = response.meta['item']
        comments = []
        soup = BeautifulSoup(response.text, 'html.parser')
        comment_list = soup.findAll('li', attrs={'class': 'comment_list'})
        for i in comment_list:
            description = i.find('span', attrs={'itemprop': 'description'}).text.strip()
            comments.append(description)
        item['comments'] = comments
        yield item
