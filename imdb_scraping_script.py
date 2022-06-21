from genericpath import exists
import os, sys

if __name__ == '__main__':
    os.chdir("webscraping")
    if not exists('imdb.json'):
        os.system("scrapy crawl imdb -o imdb.json")
