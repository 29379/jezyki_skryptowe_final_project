from matplotlib.font_manager import json_dump
from requests import get
from bs4 import BeautifulSoup
import json


if __name__ == '__main__':
    base_url = "https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page={}"
    with open('filmweb.json', 'w') as f:
        movies = []
        page_num = 0
        while page_num < 20:
            page_num += 1
            url = base_url.format(page_num)
            page = get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            hits_item_lists = soup.find_all(class_='hits__item')
            for elem in hits_item_lists:
                try:
                    title = elem.select_one('[class^=filmPreview__originalTitle]').text
                    year = elem.find(class_='filmPreview__year').text
                    rating = elem.find(class_='rateBox__rate').text
                    rating = rating.replace(',', '.')
                    dir_n_act = elem.find("span", {"itemprop": "name"}).text
                    poster = elem.find(class_='poster poster--auto')['data-image']
                    if title is not None\
                            and year is not None\
                            and rating is not None\
                            and dir_n_act is not None\
                            and poster is not None:
                        movie = {
                            'title': title,
                            'release_year': year,
                            'directors_and_actors': dir_n_act,
                            'user_rating': rating,
                            'poster': poster,
                        }
                        movies.append(movie)
                    else:
                        pass
                except:
                    continue
        f.write(json.dumps(movies))
        f.close()
