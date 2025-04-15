import bs4.element
import requests
from bs4 import BeautifulSoup, NavigableString, PageElement


def get_page(link: str) -> BeautifulSoup:
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'
    }
    r = requests.get(link, headers=header)
    html = BeautifulSoup(r.content, 'lxml')
    return html


def page_chooser(_url=None):
    if _url is None:
        _url = 'https://rezka.ag/'
    if _url.__contains__('html'):
        _pg = Page(get_page(_url))
    else:
        _pg = CardsGenerator(get_page(_url))
    return _pg


class Page:
    """Парсер данных из странички тайтла"""

    def __init__(self, html: BeautifulSoup):
        self.__html = html

    def attributes(self) -> dict:
        rows = self.__html.find('table').find_all('tr')
        res = dict()
        for row in rows:
            cells = row.find_all('td')
            res[cells[0].find('h2').text.strip()] = self.recursive_finder(cells[-1])
        for k, v in res.items():
            if k in v:
                v.remove(k)
        return res

    def recursive_finder(self, node, results=None) -> list:
        if results is None:
            results = []
        if node.name == 'a':
            results.append([node.text.strip(), node.get('href', '') if node.get('href', '').startswith('h') else (
                    'https://rezka.ag' + node.get('href', ''))])
        elif isinstance(node, NavigableString):
            if node.strip() != '' and node.strip() != ':' and node.strip() != ',':
                results.append(node.strip())
        elif node.contents:
            for child in node.children:
                # print(child.text)
                self.recursive_finder(child, results)
        else:
            results.append(node.text.strip())
        return results


class CardsGenerator:
    def __init__(self, html: BeautifulSoup):
        self.__html = html

    def cards(self):
        res = list()
        for __card in self.__html.find_all('div', attrs={'class': 'b-content__inline_item'}):
            res.append(Card(__card))
        return res


class Card:
    # Парсер карточек из страницы выбора
    # На вход принимает тег карточки
    def __init__(self, html: PageElement | bs4.Tag):
        self._html = html

    def get_img(self) -> bytes:
        link = self._html.find('img').get('src', '')
        byte_array = requests.get(link).content
        return byte_array

    def get_link(self) -> str:
        return self._html.find(attrs={'class': 'b-content__inline_item-link'}).find('a').get('href', '')

    def get_name(self) -> str:
        return self._html.find(attrs={'class': 'b-content__inline_item-link'}).find('a').text

    def get_attrs(self) -> str:
        return self._html.find(attrs={'class': 'b-content__inline_item-link'}).find('div').text

    def attributes(self) -> dict[str, str]:
        res = dict()
        res['Иконка'] = self.get_img()
        res['Ссылка'] = self.get_link()
        res['Название'] = self.get_name()
        res['Аттрибуты'] = self.get_attrs()
        return res


if __name__ == '__main__':
    url = 'https://rezka.ag/'
    pg = page_chooser(url)
    i = 1
    for card in pg.cards():
        print(f'{i}) {card.get_name():50} : {card.get_attrs()}')
        i += 1
