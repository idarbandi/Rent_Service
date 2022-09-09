from abc import abstractmethod, ABC
from config import *
from khayyam.jalali_datetime import JalaliDatetime
from parser import AdvParser
from storage import MongoStorage, FileStorage
from read import MongoRead, FileRead


class BaseCrawl(ABC):

    def __init__(self):
        self.storage = self.__store_Engine()
        self.read = self.__read_Engine()

    @staticmethod
    def __read_Engine():
        if protocols['read_type'] == 'file':
            return FileRead()
        if protocols['read_type'] == 'mongo':
            return MongoRead()
        else:
            print('wrong read Type')

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


class PageCrawler(BaseCrawl):

    def __init__(self, loc=cities, baseurl=base_url):
        self.Loc = loc
        self.baseurl = baseurl
        super().__init__()

    def finder(self, url):
        """crawl = soup.find_all
        ('span', attrs={'class': 'result-hood'})"""

        soup = BeautifulSoup(link_generator(url), 'html.parser')
        crawl = soup.find_all('a', attrs={'class': 'hdrlnk'})
        return crawl

    def start(self):
        counter = 0
        links = list()
        for city in cities:
            for base in self.finder(base_url.format(City=city)):
                if protocols['data-store']:
                    if protocols['storage_type'] == 'mongo':
                        self.storage.store([{"url": base.get('href'), 'flag': False}], 'purelink')
                    elif protocols['storage_type'] == 'file':
                        self.storage.store(f"\n{base.get('href')}", 'purelink')
                counter += 1
                links.extend(base)
            print(f'{counter} Houses/Apartments Crawled Outta {city} for rent')
            counter = 0
        print('crawling is finished')
        return "DONE"


class DataCrawler(BaseCrawl):
    def __init__(self):
        super().__init__()
        self.links = self.read.read('purelink')
        self.parser = AdvParser()

    def start(self):
        link = self.links
        for i in range(len(link)):
            pure = link_generator(link[i])
            data = self.parser.parser(pure)
            if protocols['data-store']:
                self.storage.store(data, 'Encoded.Data')
            print(f'{len(pure)} data Decoded successfully at {str(JalaliDatetime.today())}')
