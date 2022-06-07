# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WebscrapingPipeline:
    def process_item(self, item, spider):
        return item


#   ??? AGAIN ???
"""
from webapp.webapp.models import Data
from unidecode import unidecode


class ImdbPipeline:
    def process_item(self, item, spider):
        title = unidecode(item['title'])
        release_year = unidecode(item['release_year'])
        directors_and_actors = unidecode(item['directors_and_actors'])
        user_rating = unidecode(item['user_rating'])
        poster = unidecode(item['poster'])

        Data.objects.create(
            title=title,
            release_year=release_year,
            directors_and_actors=directors_and_actors,
            user_rating=user_rating,
            poster=poster,
        )

        return item
"""
