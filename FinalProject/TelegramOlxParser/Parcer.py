


import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'

HOST = 'https://www.olx.ua/'
URL = 'https://www.olx.ua/uk/transport/'

HEADERS = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='css-1sw7q4x')
    cards = []

    for item in items:
        title_item = item.find_next('h6', class_='css-16v5mdi er34gjf0')
        title = title_item.get_text() if title_item else None

        price_item = item.find_next('p', class_='css-10b0gli er34gjf0')
        price = price_item.get_text() if price_item else None

        gearbox_item = item.find_next('span', class_='css-efx9z5')
        gearbox = gearbox_item.get_text() if gearbox_item else None

        link_elem = item.find_next('a', class_='css-rc5s2u')
        link = link_elem.get('href') if link_elem else None
        link = HOST + str(link)

        cards.append({
            'title': title,
            'price': price,
            'gearbox': gearbox,
            'link': link
        })
    return cards
    # print(cards)
def save_to_csv(cards, path):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(['Title', 'Price', 'Gearbox', 'Link'])
        for card in cards:
            writer.writerow([card['title'], card['price'], card['gearbox'], card['link']])


def parser():
    pagination = int(input("Enter number of pages you want to parse :"))
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, pagination + 1):
            print("Parsing page " + str(page))
            html = get_html(URL, params={'page':page})
            cards.extend(get_content(html.text))
            save_to_csv(cards, CSV)
        pass
    else:
        print("Error")

parser()


# get_content(get_html(URL).text)
# print(get_html(URL))