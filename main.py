from crawler import *
import sys





if __name__ == "__main__":
    p = input('Press p To Continue .... ')
    p = sys.argv
    if p == p:
        #MeCrawler = PageCrawler()
        #print(MeCrawler.start())
        #print(MeCrawler.store())
        Ucrawler = DataCrawler()
        Ucrawler.store()
