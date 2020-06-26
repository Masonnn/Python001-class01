import scrapy


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyanMovies.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
