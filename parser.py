from bs4 import BeautifulSoup


class AdvParser:

    def parser(self, html_data):
        soup = BeautifulSoup(html_data, 'html.parser')
        data = dict(
            title=None,
            housing=None,
            price=None,
            small_title=None,
            post_id=None,
            created_time=None
        )

        title_tag = soup.find('span', attrs={'id': 'titletextonly'})
        if title_tag:
            data['title'] = title_tag.text

        housing_tag = soup.find('span', attrs={'class': 'housing'})
        if housing_tag:
            data['housing'] = housing_tag.text.replace('/ ', '')


        price_tag = soup.find('span', attrs={'class': 'price'})
        if price_tag:
            data['price'] = price_tag.text


        small_tag = soup.find('small')
        if small_tag:
            data['small_title'] = small_tag.text.replace(' ', '')


        # body_tag = soup.select_one('#postingbody')
        # if body_tag:
        #     data['body'] = body_tag.text.replace('\n\nQR Code Link to This Post\n\n\n', '')

        selector1 ='body > section > section > section > div.postinginfos > p:nth-child(1)'
        id_tag = soup.select_one(selector1)
        if id_tag:
            data['post_id'] = id_tag.text.replace('Id publi: ', '')


        selector2 = 'body > section > section > section > div.postinginfos > p.postinginfo.reveal > time'
        create_tag = soup.select_one(selector2)
        if create_tag:
            data['created_time'] = create_tag.text

        return data