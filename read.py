from abc import abstractmethod, ABC
from mongo import MongoDB
from khayyam import jalali_datetime


class ReadBase(ABC):

    @abstractmethod
    def read(self, filename, collection, *args):
        pass


class FileRead(ReadBase):

    def read(self, filename, *args):
        with open(f"Storage/{filename}.json", "r") as readlist:
            data = readlist.readlines()
            return data


class MongoRead(ReadBase):

    def __init__(self):
        self.mongo = MongoDB()

    def read(self, collection, *args):
        links = list()
        collect = self.mongo.db["purelink"]
        for x in collect.find({'flag': False}):
            links.append(x["url"])
            collect.update_one({'_id': x['_id']}, {'$set': {'flag': True}})
        print('flags updated')
        return links

    def __str__(self):
        return f'data crawled successfully at {jalali_datetime.JalaliDatetime.today()}'
