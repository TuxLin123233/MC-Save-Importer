import json

data = {
    'name': 'Erzong'
}

with open("./data.json", encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)