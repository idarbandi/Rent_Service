import requests
from bs4 import BeautifulSoup

base_url = 'https://{City}.craigslist.org/search/apa?lang=en&cc=gb'

cities = ['paris', 'brussels', 'brighton', 'liverpool', 'oxford', 'cambridge', 'manchester', 'belfast']

protocols = {
    'Link_Pick': True,
}

def link_generator(kir):
    response = requests.get(kir)
    return response.text


def linkpicker(func,kire):
    if protocols['Link_Pick']:
        soup = BeautifulSoup(link_generator(kire), 'html.parser')
        return soup.find_all('a', attrs={'class': 'hdrlnk'})
    return func
