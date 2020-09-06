import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from time import sleep

from Spiders.items import SpidersItem


class PhonesSpider(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['smzdm.com']

    # start_urls = ['http://smzdm.com/']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = "https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        phones = Selector(response=response).xpath('//h5[@class="feed-block-title"]')
        print("================================phones")
        print(phones)
        print(type(phones))
        print(len(phones))
        for phone in phones:
            item = SpidersItem()
            prd_name = phone.xpath('./a/text()').extract_first().strip()
            link = phone.xpath('./a/@href').extract()[0]
            item['prd_name'] = prd_name
            item['link'] = link

            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse_comments)

    def parse_comments(self, response):
        selector = Selector(response=response)
        item = response.meta['item']

        try:
            # # comments = selector.xpath('//span[@itemprop="description"]/text()').getall()
            # prd_name = selector.xpath('//h1[@class="title J_title"]/text()').extract_first().strip('\n').strip()
            # link = response.url
            # item['prd_name'] = prd_name
            # item['link'] = link
            comments = selector.xpath('//span[@itemprop="description"]/text()').getall()
            new_comments = list(set(comments))
            for comment in new_comments:
                item = response.meta['item']
                item['comments'] = comment.strip()
                yield item
        except Exception:
            print("==========================该商品没有评论==========================")
        finally:
            print("==========================没评论商品入库==========================")
            yield item

        urls = selector.xpath('//*[@id="commentTabBlockNew"]/ul/li[not(@class)]/a[not(@class)]/@href').extract()
        for next_page in urls:
            yield scrapy.Request(url=next_page, meta={'item': item}, callback=self.parse_comments)

    # 使用webdriver模拟翻页
    # driver = webdriver.Chrome()
    # driver.get(response.url)
    #
    # try:
    #     pagedown = driver.find_element_by_class_name('pagedown')
    #     while pagedown:
    #         driver.implicitly_wait(10)
    #         pagedown.click()
    #         yield scrapy.Request(url=driver.current_url, meta={'item': item}, callback=self.parse_comments)
    #         driver.implicitly_wait(5)
    #         try:
    #             pagedown = driver.find_element_by_class_name('pagedown')
    #         except Exception:
    #             print("已获取完所有评论")
    #             break
    # except Exception:
    #     print("评论不超过1页，无需翻页")
    #     pass
    # finally:
    #     driver.quit()
