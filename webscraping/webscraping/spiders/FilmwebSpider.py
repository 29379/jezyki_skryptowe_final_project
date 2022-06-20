from requests import request
import scrapy, os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pathlib import Path


"""PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
filmweb_file = os.path.join(PROJECT_DIR, 'webscraping/filmweb.json')"""


class FilmwebSpider(scrapy.Spider):
    name = 'filmweb'
    allowed_domains = ["filmweb.pl"]
    start_urls = ["https://www.filmweb.pl/films/search"]

    def parse(self, response, **kwargs):
        for film in response.css("li.hits__item"):
            year = film.css("div.filmPreview__year::text").get()
            dir_n_act = film.css("div.filmPreview__info.filmPreview__info--directors > ul > li a::attr(title)").get()
            poster = film.css("div.poster.poster--auto::attr(data-image)").get()
            rating = film.css("span.rateBox__rate::text").get()
            title = film.css("h2.filmPreview__title::text").get()
            if year is not None\
             and dir_n_act is not None\
                 and poster is not None\
                     and rating is not None\
                         and title is not None:
                yield {
                    'title': title,
                    'release_year': year,
                    'directors_and_actors': dir_n_act,
                    'user_rating': rating,
                    'poster': poster,
                }
            else:
                pass


"""class FilmwebSpider(CrawlSpider):
    name = 'filmweb'
    allowed_domains = ["filmweb.pl"]
    start_urls = ["https://www.filmweb.pl/films/search"]

    #l_extr_movie = LinkExtractor(allow=())
    l_extr_next = LinkExtractor(restrict_css="pagination__item")

    movie_rule = Rule(
        #l_extr_movie,
        callback="parse_item",
        follow= False)
    next_page_rule = Rule(
        l_extr_next,
        follow= True)

    rules = (
        movie_rule, next_page_rule,
    )

    def parse_item(self, response):
        for film in response.css("li.hits__item"):
            year = film.css("div.filmPreview__year::text").get()
            dir_n_act = film.css("div.filmPreview__info.filmPreview__info--directors > ul > li a::attr(title)").get()
            poster = film.css("div.poster.poster--auto::attr(data-image)").get()
            rating = film.css("span.rateBox__rate::text").get()
            title = film.css("h2.filmPreview__title::text").get()
            if year is not None\
             and dir_n_act is not None\
                 and poster is not None\
                     and rating is not None\
                         and title is not None:
                yield {
                    'title': title,
                    'release_year': year,
                    'directors_and_actors': dir_n_act,
                    'user_rating': rating,
                    'poster': poster,
                }
            else:
                pass"""


"""class FilmwebSpider(scrapy.Spider):
    name = 'filmweb'
    allowed_domains = ["filmweb.pl"]
    start_urls = ["https://filmweb.pl/films/search"]
    base_url = "https://filmweb.pl/films/search/"

    l_extr_next = LinkExtractor(allow=(), restrict_xpaths=('//a[@class="pagination__link"]'))

    movie_rule = Rule(
        l_extr_next,
        callback="parse",
        follow= True)


    rules = (
        movie_rule,
    )

    def parse(self, response):
        try:
            f = open(filmweb_file, 'a')
            for film in response.css("li.hits__item"):
                year = film.css("div.filmPreview__year::text").get()
                dir_n_act = film.css("div.filmPreview__info.filmPreview__info--directors > ul > li a::attr(title)").get()
                poster = film.css("div.poster.poster--auto::attr(data-image)").get()
                rating = film.css("span.rateBox__rate::text").get()
                title = film.css("h2.filmPreview__title::text").get()
                if year is not None\
                    and dir_n_act is not None\
                    and poster is not None\
                    and rating is not None\
                    and title is not None:
                        f.write ({
                            'title': title,
                            'release_year': year,
                            'directors_and_actors': dir_n_act,
                            'user_rating': rating,
                            'poster': poster,
                        })
                else:
                    pass
                next_page = response.xpath('//a[@class="pagination__link"]/@href').extract()
                if next_page:
                    next_href = next_page[0]
                    next_page_url = 'filmweb.pl' + next_href
                    request = scrapy.Request(url=next_page_url)
                    yield request
        except FileNotFoundError:
            pass
        """