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
        for x in collect.find({}, {"_id": 0}):
            links.append(x["url"])
        return links

    def __str__(self):
        return f'data crawled successfully at {jalali_datetime.JalaliDatetime.today()}'
