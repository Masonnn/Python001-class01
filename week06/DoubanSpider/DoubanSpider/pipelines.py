# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

createTable = """CREATE TABLE IF NOT EXISTS`doubanMovies` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `film_name` varchar(100) NOT NULL,
  `film_stars` int(100) NOT NULL,
  `film_shorts` varchar(3000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""


class DoubanspiderPipeline:

    def __init__(self):
        print("=============init=============")
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  # 使用自己的用户名
            passwd='1qaz@WSX',  # 使用自己的密码
            db='Scrapy_learn',  # 数据库名
            charset='utf8'
        )
        self.cursor = self.connect.cursor()
        print("===============createTable=================")
        self.cursor.execute(createTable)

    def process_item(self, item, spider):
        self.cursor.execute(
            """INSERT INTO doubanMovies (film_name, film_stars, film_shorts) VALUES (%s, %s, %s)""",
            (item['film_name'], item['film_stars'], item['film_shorts']))
        self.connect.commit()
        # self.cursor = self.connect.close()

        return item

