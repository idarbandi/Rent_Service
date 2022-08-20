import requests
import threading
from time import sleep




def Ping(url):
    response = requests.get(url)
    sleep(4)
    return response


links = {
    'www.google.com',
    'www.7learn.ac',
    'www.yahoo.com'
}

if __name__ == "__main__":
    for link in links:
        res = Ping(link)