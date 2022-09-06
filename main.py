from crawler import *
import sys





if __name__ == "__main__":
    p = sys.argv
    p = input('Press "1" to initiate link Crawler'
                  ' and press "2" to initiate data crawler .... ')

    if p == '1':
        Crawler = PageCrawler()
        print(Crawler.start())
    if p == '2':
        Ucrawler = DataCrawler()
        Ucrawler.start()