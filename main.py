from crawler import *
import sys
from image import ImageDownloader

if __name__ == "__main__":
    p = sys.argv
    p = input('Press "1" to initiate link Crawler'
              ' and press "2" to initiate data crawler and "3" to Image Crawler .... ')

    if p == '1':
        Crawler = PageCrawler()
        print(Crawler.start())
    if p == '2':
        Crawler = DataCrawler()
        Crawler.start()
    if p == '3':
        Crawler = ImageDownloader()
        Crawler.start()
