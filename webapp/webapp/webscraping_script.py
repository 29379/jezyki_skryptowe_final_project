import os, sys

os.chdir("../../")
os.system("ls")
os.chdir("webscraping")
os.system("scrapy crawl imdb")
