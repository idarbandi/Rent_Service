from abc import abstractmethod, ABC
from config import *
from khayyam import jalali_datetime
from time import sleep
from parser import AdvParser
from storage import MongoStorage, FileStorage


class BaseCrawl(ABC):

    def __init__(self):
        self.storage = self.__store_Engine()

    @staticmethod
    def __store_Engine():
        if protocols['storage_type'] == 'file':
            return FileStorage()
        if protocols['storage_type'] == 'mongo':
            return MongoStorage()
        else:
            print('wrong storage type chosen')

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def store(self):
        pass


class PageCrawler(BaseCrawl):

    def __init__(self, loc=cities, baseurl=base_url):
        self.Loc = loc
        self.baseurl = baseurl
        super().__init__()

    def finder(self, url):
        ''''crawl = soup.find_all
        ('span', attrs={'class': 'result-hood'})'''

        soup = BeautifulSoup(link_generator(url), 'html.parser')
        crawl = soup.find_all('a', attrs={'class': 'hdrlnk'})
        return crawl

    def start(self):
        counter = 0
        links = list()
        for city in cities:
            for link in self.finder(base_url.format(City=city)):
                counter += 1
                links.extend(link)
            print(f'{counter} Houses/Apartments Crawled Outta {city} for rent')
            counter = 0
        return 'crawling is finished'

    def store(self):
        print('Storing Please wait ....')
        sleep(3)
        for city in cities:
            base = self.finder(base_url.format(City=city))
            with open('Storage/data.json', 'a+') as Jason:
                for lnk in base:
                    Jason.writelines(f"\n{lnk.get('href')}")
                Jason.close()
        return 'Storage Complete'


class DataCrawler(BaseCrawl):
    def __init__(self):
        self.links = self.getdata()
        self.parser = AdvParser()
        super().__init__()

    @staticmethod
    def getdata():
        with open("Storage/data.json", "r") as readlist:
            data = readlist.readlines()
            return data

    def start(self):
        link = self.links
        for i in range(len(link)):
            pure = link_generator(link[i])
            data = self.parser.parser(pure)
            if protocols['data-store']:
                self.storage.store(data, str(jalali_datetime.datetime.now()))
            print(i for i in range(len(data)))
        return f'data crawled successfully at {jalali_datetime.JalaliDatetime.today()}'

    def store(self):
        pass
