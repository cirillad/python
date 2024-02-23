import json
import os


def get_file_json(name_file: str = 'data.json', key_id: str = '4e17384a-567e-4af9-8b7d-62446debf1ac'):
    with open(name_file, 'r') as f:
        data = json.load(f)[key_id]

    with open(key_id, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    os.rename(key_id, f'{key_id}.json')

    return f'{key_id}.json'