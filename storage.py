from mongo import MongoDB
from abc import ABC, abstractmethod
import json


class StorageBase(ABC):

    @abstractmethod
    def store(self, data, filename, *args):
        pass


class MongoStorage(StorageBase):

    def __init__(self):
        self.mongo = MongoDB()

    def store(self, data, *args):
        collection = getattr(self.mongo.db, 'collection')
        collection.insert_one(data)


class FileStorage(StorageBase):

    def store(self, data, filename, *args):
        pure = open(f'Storage/Data_Crawlage/{filename}.json', 'w')
        pure.write(json.dumps(data))
        pure.close()
