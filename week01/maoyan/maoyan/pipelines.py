# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_genre = item['film_genre']
        play_date = item['play_date']
        output = f'|{film_name}|\t|{film_genre}|\t|{play_date}|\n'
        with open('./maoyanMovie.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
