import requests
from bs4 import BeautifulSoup

URL = 'https://www.avito.ru/krasnodarskiy_kray/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
          'accept': '*/*'}
        
HOST = 'https://www.avito.ru'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="iva-item-content-m2FiN")
    print(items)

    cars =[]
    for item in items:
        cars.append({
            'title': item.find('h3', itemprop="name").get_text(),
            'link': HOST + item.find('a', itemprop="url").get('href'),
            'price': item.find('span', class_="price-text-1HrJ_ text-text-1PdBw text-size-s-1PUdo").get_text().replace('\xa0₽', ''),
       
        })
        return cars
#основная ф-ция
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = get_content(html.text)
    else:
        print('Error')

parse()