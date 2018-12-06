#!/usr/bin/env python3.7
import unicodedata
from urllib.request import urlopen

import yaml
from bs4 import BeautifulSoup

URL = "http://www.marktplaats.nl/verkopers/15321101.html"+"?view=gv"
YML = 'data.yml'

print("Scraped URL: {}".format(URL))
print("Ouput: {}".format(YML))
print("RESULTS:")

def iter_cards(html):
    soup = BeautifulSoup(html, "html5lib")
    cards = soup.findAll("div", {"class": "mp-Listing-card-flex mp-Listing-card-flex--landscape"})

    for i, card in enumerate(cards):
        money_data = card.find("span", {"class": "price-new"}).get_text()
        normalized_money_data = unicodedata.normalize("NFKD", money_data)
        html_money = normalized_money_data.replace('€', '&euro;').strip()

        index_string = 'id_{}'.format(i)
        case = {
            'price': html_money,
            'link': card.a.attrs['href'].partition('?')[0],
            'img': 'http:{}'.format(card.img.attrs['src']),
            'title': card.img.attrs['alt']
        }

        print(index_string)

        yield (index_string, case)

if __name__ == '__main__':
    html = urlopen(URL).read()
    cards = {'items': dict(iter_cards(html))}
    with open(YML, 'w') as outfile:
        yaml.dump(cards, outfile, default_flow_style=False)
