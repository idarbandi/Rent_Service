from abc import abstractmethod, ABC
from config import url, cities
import requests
from bs4 import BeautifulSoup
import json



class BaseCrawl(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def store(self):
        pass


class PageCrawler(BaseCrawl):

    def __init__(self, loc=cities, baseurl=url):
        self.Loc = loc
        self.baseurl = baseurl



    def start(self):
        List = None
        counter = 0
        for city in cities:
            response = requests.get(url.format(City=city))
            soup = BeautifulSoup(response.text, 'html.parser')
            crawl = soup.find_all('span', attrs={'class': 'result-hood'})
            for link in crawl:
                counter+=1
            print(f'{counter} Houses Crawled Outta {city}')
            counter=0
        return '__crawling_Done__'








    def store(self):
        pass



class DataCrawler(BaseCrawl):
    def start(self):
        pass

    def store(self):
        pass
