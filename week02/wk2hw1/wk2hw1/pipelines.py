# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql

createTable = """CREATE TABLE IF NOT EXISTS`maoyanMovies` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `film_name` varchar(100) NOT NULL,
  `film_genre` varchar(255) NOT NULL,
  `play_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""


class Wk2Hw1Pipeline(object):

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

    def process_item(self, item, spider):
        self.cursor.execute(createTable)
        self.cursor.execute(
            """INSERT INTO maoyanMovies (film_name, film_genre, play_date) VALUES (%s, %s, %s)""",
            (item['film_name'], item['film_genre'], item['play_date']))
        self.connect.commit()
        # self.cursor = self.connect.close()

        return item
