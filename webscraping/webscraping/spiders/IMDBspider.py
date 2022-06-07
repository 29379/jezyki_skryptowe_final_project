import scrapy

"""
REQUIRED FUNCTIONS FOR BASIC WEBSCRAPING:
     *  extract / request
     *  transform / parse
     *  load / output
"""


class IMDBspider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    def parse(self, response, **kwargs):
        """Simple parsing function"""
        #   'yield' is used like 'return', but the function returns a GENERATOR
        #   which are iterators you can only iterate over once, that do not store
        #   values in memory, but generate them on the fly
        #   'yield' is most commonly used in scrapy instead of 'return'
        i = -1
        for films in response.css("tr"):
            year = films.css("span.secondaryInfo::text").get()
            dir_n_act = films.css('a::attr(title)').get()
            poster = films.css('img::attr(src)').get()
            if year is not None and dir_n_act is not None:
                i += 1
                title = films.xpath('//td[@class="titleColumn"]/a/text()').getall()[i]
                rating = films.xpath('//td[@class="ratingColumn imdbRating"]/strong/text()').getall()[i]
                yield {
                    'title': title,
                    'release_year': year,
                    'directors_and_actors': dir_n_act,
                    'user_rating': rating,
                    'poster': poster,
                }
            else:
                pass
