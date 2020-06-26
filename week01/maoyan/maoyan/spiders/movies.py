import scrapy
# from bs4 import BeautifulSoup
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    # start_urls = ['http://maoyan.com/']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 处理字符串

        def parse_text(str):
            return str.strip().split('\n')[-1].strip()

        bs_info = BeautifulSoup(response.text, 'html.parser')
        for tagslevel1 in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
            for tagslevel2 in tagslevel1.find_all('div', attrs={'class': 'movie-hover-title'}):
                for i in tagslevel2.find_all('span', attrs={'class': 'hover-tag'}):

                    item = MaoyanItem()
                    if i.text == '类型:':
                        film_genre = parse_text(i.parent.text)
                    if i.text == '上映时间:':
                        play_date = parse_text(i.parent.text)
                        film_name = parse_text(
                            i.find_parent('div').get('title'))
                        item['film_name'] = film_name
                        item['play_date'] = play_date
                        item['film_genre'] = film_genre
                    yield item
