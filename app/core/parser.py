import bs4
from bs4 import BeautifulSoup


class Parser:
    def parse_movies(self, html: str):
        soup = BeautifulSoup(html, 'lxml')
        movies = []
        items = soup.select('.b-content__inline_item')

        for item in items:
            movies.append(Card(item))

        return movies


class Card:
    def __init__(self, html: bs4.Tag):
        self._html = html

    def get_img_link(self):
        return self._html.find('img').get('src', '')

    def get_link(self):
        return self._html.select_one('b-content__inline_item-link').find('a').get('href', '')

    def get_name(self):
        return self._html.select_one('b-content__inline_item-link').find('a').text

    def get_attrs(self) -> str:
        return self._html.select_one('b-content__inline_item-link').find('div').text

