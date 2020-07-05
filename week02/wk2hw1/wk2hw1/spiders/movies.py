import scrapy
from scrapy.selector import Selector
from wk2hw1.items import Wk2Hw1Item


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']

    # start_urls = ['http://maoyan.com/']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        item = Wk2Hw1Item()

        for movie in movies:
            film_name = movie.xpath('./div[1]/span/text()').extract()

            film_genre = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
            play_date = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip()
            item['film_name'] = film_name
            item['play_date'] = play_date
            item['film_genre'] = film_genre

            yield item
