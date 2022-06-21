import os, sys

if __name__ == '__main__':
    os.chdir("/home/Kuba/Desktop/tmp/jezyki_skryptowe_final_project/webscraping/")
    os.system("python TomatoesSpider.py -o tomatoes.json")