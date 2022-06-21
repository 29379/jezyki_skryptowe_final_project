from genericpath import exists
import os, sys

if __name__ == '__main__':
    os.chdir("/home/Kuba/Desktop/tmp/jezyki_skryptowe_final_project/webscraping/")
    if not exists('/home/Kuba/Desktop/tmp/jezyki_skryptowe_final_project/webscraping/imdb.json'):
        os.system("scrapy crawl imdb -o imdb.json")
