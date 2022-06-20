import scrapy


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
        for film in response.css("tr"):
            year = film.css("span.secondaryInfo::text").get()
            dir_n_act = film.css('a::attr(title)').get()
            poster = film.css('img::attr(src)').get()
            if year is not None and dir_n_act is not None:
                i += 1
                title = film.xpath('//td[@class="titleColumn"]/a/text()').getall()[i]
                rating = film.xpath('//td[@class="ratingColumn imdbRating"]/strong/text()').getall()[i]
                yield {
                    'title': title,
                    'release_year': year,
                    'directors_and_actors': dir_n_act,
                    'user_rating': rating,
                    'poster': poster,
                }
            else:
                pass
