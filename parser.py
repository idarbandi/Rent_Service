from bs4 import BeautifulSoup


class AdvParser:

    def parser(self, html_data):
        soup = BeautifulSoup(html_data, 'html.parser')
        data = dict(
            title=None,
            housing=None,
            price=None,
            small_title=None,
            body=None,
            post_id=None,
            created_time=None
        )

        title_tag = soup.find('span', attrs={'id': 'titletextonly'})
        if title_tag:
            data['title'] = title_tag

        housing_tag = soup.find('span', attrs={'class': 'housing'})
        if housing_tag:
            data['housing'] = housing_tag.text


        price_tag = soup.find('span', attrs={'class': 'price'})
        if price_tag:
            data['price'] = price_tag.text


        small_tag = soup.find('small')
        if small_tag:
            data['small_title'] = small_tag.text


        body_tag = soup.select_one('#postingbody')
        if body_tag:
            data['body'] = body_tag.text

        title_tag = soup.find('span', attrs={'id': 'titletextonly'})
        if title_tag:
            data['title'] = title_tag.text

        #id_tag = soup.find('font', attrs={'style', 'inherit'}) #Publish ID: 7526537308
        #if id_tag:
        #    data['post_id'] = id_tag.text

        create_tag = soup.find('time', attrs={'class': 'date timeago'})
        if create_tag:
            data['created_time'] = create_tag.text

        return data
