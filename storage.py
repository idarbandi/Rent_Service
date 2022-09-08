from mongo import MongoDB
from abc import ABC, abstractmethod
import json
from time import sleep


class StorageBase(ABC):

    @abstractmethod
    def store(self, data, filename, *args):
        pass


class MongoStorage(StorageBase):

    def __init__(self):
        self.mongo = MongoDB()

    def store(self, data, collec, *args):
        collection = getattr(self.mongo.db, collec)
        collection.insert_many(data)


class FileStorage(StorageBase):



    def store(self, data, filename, *args):
        if filename == 'purelink':
            print('Storing links Please wait ....')
            with open('Storage/purelink.json', 'a+') as Jason:
                Jason.writelines(data)
                Jason.close()
            print('Link Storage Complete')
        else:
            pure = open(f'Storage/Data_Crawlage/{filename}.json', 'w')
            pure.write(json.dumps(data))
            pure.close()

