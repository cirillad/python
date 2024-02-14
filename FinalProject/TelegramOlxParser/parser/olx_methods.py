import json
import random
import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

URL = 'https://www.olx.ua/uk/transport/'

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_main_page_with_items():
    base_url = 'https://www.olx.ua'

    any_page = random.randint(1, 50)

    responce = requests.get(url=URL, headers=HEADERS, params={'page': any_page})

    soup = BeautifulSoup(responce.text, 'lxml')

    list_cars = soup.find('div', class_='css-oukcj3')

    url_links_transport = []

    urls = list_cars.find_all('a', class_='css-rc5s2u')

    for url in urls:
        piece_of_url = url['href']
        main_url = base_url + piece_of_url

        url_links_transport.append(main_url)

    return url_links_transport


def get_page_with_data(url):
    responce = requests.get(url=url, headers=HEADERS)

    soup = BeautifulSoup(responce.text, 'lxml')

    price = soup.find('h3', class_='css-12vqlj3')

    title = soup.find('h4', class_='css-1juynto')

    user_name = soup.find('h4', class_='css-1lcz6o7 er34gjf0')

    publication = soup.find('span', class_='css-fscvqi er34gjf0')

    description = soup.find_all('li', class_='css-1r0si1e')

    list_options = []

    for element in description:
        option = element.find('p', class_='css-b5m1rv er34gjf0')
        list_options.append(option.text)

    description = ', '.join(list_options)

    div_photo = soup.find_all('img')

    photos = []

    for photo in div_photo:
        if 'https://ireland' in photo['src']:
            photos.append(photo['src'])


    list_data = [title.text, price.text, user_name.text, publication.text, description, photos]

    return list_data


def add_to_json(json_data, id_item):
    # Открываем файл на чтение
    filename = "data.json"
    with open(filename, "r") as file:
        # Загружаем данные из файла в словарь
        data = json.load(file)

    # Обновляем словарь данными из параметра json_data
    data[id_item] = json_data

    # Записываем обновленные данные обратно в файл
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

    print('Добавлено в файл')