import os, sys

if __name__ == '__main__':
    os.chdir("webscraping")
    os.system("python FilmwebSpider.py -o filmweb.json")