import os, sys

if __name__ == '__main__':
    os.chdir("../../")
    os.system("ls")
    os.chdir("/home/Kuba/Desktop/tmp/jezyki_skryptowe_final_project/webscraping/")
    os.system("scrapy crawl imdb -o imdb.json")
