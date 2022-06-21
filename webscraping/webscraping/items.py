# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    release_year = scrapy.Field()
    directors_and_actors = scrapy.Field()
    user_rating = scrapy.Field()
    poster = scrapy.Field()
