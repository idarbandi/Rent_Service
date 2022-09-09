from bs4 import BeautifulSoup


class AdvParser:

    def __init__(self):
        self.soup = None

    @property
    def title(self):
        title_tag = self.soup.find('span', attrs={'id': 'titletextonly'})
        if title_tag:
            return title_tag.text
        return None

    @property
    def area(self):
        housing_tag = self.soup.find('span', attrs={'class': 'housing'})
        if housing_tag:
            return housing_tag.text.replace('/ ', '')
        return None

    @property
    def price(self):
        price_tag = self.soup.find('span', attrs={'class': 'price'})
        if price_tag:
            return price_tag.text
        return None
    @property
    def small_title(self):
        small_tag = self.soup.find('small')
        if small_tag:
             return small_tag.text.replace(' ', '')
        return None


        # body_tag = soup.select_one('#postingbody')
        # if body_tag:
        #     data['body'] = body_tag.text.replace('\n\nQR Code Link to This Post\n\n\n', '')




    @property
    def post_id(self):
        selector = 'body > section > section > section > div.postinginfos > p:nth-child(1)'
        id_tag = self.soup.select_one(selector)
        if id_tag:
            id_tag = id_tag.text.replace('Id publi: ', '')
            return id_tag.replace('post id:', '')
        return None

    @property
    def created_time(self):
        time_selector = 'body > section > section > section > div.postinginfos > p:nth-child(2) > time'
        time = self.soup.select_one(time_selector)
        if time:
            return time.attrs['datetime']

    @property
    def image(self):
        img_tag = self.soup.find_all('img')
        images_sources = set([img.attrs['src'].replace('50x50c', '600x450') for img in img_tag])
        return [{"url": src, 'flag': False} for src in images_sources]

    def parser(self, html_data):
        self.soup = BeautifulSoup(html_data, 'html.parser')
        data = dict(
            title=self.title, price=self.price, area=self.area,
            allias=self.small_title, post_id=self.post_id,
            created_time=self.created_time, images=self.image
        )
        return data

