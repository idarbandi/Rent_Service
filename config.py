import requests
from bs4 import BeautifulSoup

base_url = 'https://{City}.craigslist.org/search/apa?lang=en&cc=gb'

cities = ['brussels', 'brighton', 'paris', 'liverpool', 'oxford', 'cambridge', 'manchester', 'belfast']

protocols = {
    'Link_Pick': True,
    'data-store': True,
    'storage_type': 'file',  # either can be (mongo) or (file)
    'read_type': 'mongo',  # either can be (mongo) or (file)
    'image_store': True

}


def link_generator(lnk):
    response = requests.get(lnk, stream=True)
    return response.text


def linkpicker(func, kire):
    if protocols['Link_Pick']:
        soup = BeautifulSoup(link_generator(kire), 'html.parser')
        return soup.find_all('a', attrs={'class': 'hdrlnk'})
    return func
