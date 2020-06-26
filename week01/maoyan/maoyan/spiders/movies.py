import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        item = MaoyanItem()
        for movie in movies:
            film_name = movie.xpath('./div[1]/span/text()').extract()

            film_genre = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
            play_date = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip()
            item['film_name'] = film_name
            item['play_date'] = play_date
            item['film_genre'] = film_genre

            yield item
