# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pretty_errors
import csv
from scrapy.exporters import CsvItemExporter


class MaoyanPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_genre = item['film_genre']
        play_date = item['play_date']

        with open("./maoyanMovie.csv", "a+b") as f:
            exporter = CsvItemExporter(f, include_headers_line=False)
            exporter.start_exporting()
            exporter.export_item(item)
            exporter.finish_exporting()

        return item


# class SaveAsCsvPipeline:
#     def process_item(self, item, spider):
#         film_name = item['film_name']
#         film_genre = item['film_genre']
#         play_date = item['play_date']

#         output = [film_name, film_genre, play_date]

#         list1 = []
#         list1.append(output)

#         maoyanMovie = pd.DataFrame(data=list1[:10], columns=[
#                                    '电影名字', '类型', '上映日期'])

#         maoyanMovie.to_csv('./maoyanMovie.csv', mode='a+b',
#                            encoding='utf8', index=False, header=True)

#         return item
