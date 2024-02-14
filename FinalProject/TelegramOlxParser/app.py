import time
import uuid

from parser.olx_methods import get_main_page_with_items, get_page_with_data, add_to_json


def main():
    urls = get_main_page_with_items()

    dict_items = {}

    for url in urls:
        id_uuid = str(uuid.uuid4())
        try:
            x = get_page_with_data(url)

            data = {'user-name': x[2], 'title': x[0], 'price': x[1], 'publication': x[3], 'description': x[4], 'photo': x[5]}
            print(data)
            dict_items[id_uuid] = data
            add_to_json(json_data=data, id_item=id_uuid)
            print(data)

            time.sleep(0.2)
        except Exception as error:
            print(error)
            continue

    print(dict_items)


if __name__ == "__main__":
    main()