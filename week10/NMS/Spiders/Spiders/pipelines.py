# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter
import pymysql


class SpidersPipeline:
    # def process_item(self, item, spider):
    # return item

    def process_item(self, item, spider):
        print("=================== process_item in pipeline =======================")
        prd_name = item['prd_name']
        link = item['link']
        comments = item['comments']
        output = f'|{prd_name}|\t|{link}|\t|{comments}|\n\n'
        with open('./phone.txt', 'a+', encoding='utf-8') as article:
            article.write(output)

        with open("./phones.csv", "a+b") as f:
            exporter = CsvItemExporter(f, include_headers_line=False)
            exporter.start_exporting()
            exporter.export_item(item)
            exporter.finish_exporting()

        return item


class ToMysql(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',  # 使用自己的用户名
            passwd='1qaz@WSX',  # 使用自己的密码
            db='nms',  # 数据库名
            charset='utf8mb4'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """INSERT INTO phones (prd_name, link, comments) VALUES (%s, %s, %s)""",
                (item['prd_name'], item['link'], item['comments']))
            # self.cursor.close()
            self.connect.commit()
        except Exception as e:
            print("插入数据失败", e)
            # self.connect.rollback()
        # self.connect.close()
        return item
