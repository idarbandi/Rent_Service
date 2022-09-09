from crawler import BaseCrawl
import requests
from mongo import MongoDB
from config import protocols


class ImageDownloader(BaseCrawl):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.mongo = MongoDB()
        self.adv = self.__load_adv()

    def __load_adv(self):
        collection = getattr(self.mongo.db, 'Encoded.Data')
        return collection.find({})

    @staticmethod
    def get(link):
        try:
            response = requests.get(link, stream=True)
        except requests.HTTPError:
            return None
        return response

    def start(self):
        for adv in self.adv:
            counter = 1
            for image in adv['images']:
                response = self.get(image['url'])
                if protocols['image_store']:
                    self.disk(response , adv['post_id'], counter)
                counter += 1

    def disk(self, data, adv_id, NUM):
        filename = f'{adv_id}{NUM}'
        f = open(f'Storage/images/{filename}.jpg', 'ab')
        f.write(data.content)
        for _ in data.iter_content():
            f.write(data.content)
        print(f" image {filename} saved")
        return filename

