import csv
import json

def open_file(file):
    with open('data.csv', 'r', encoding='utf8') as csvfile:
        data = csv.DictReader(csvfile)
        finish_list = []
        for i in data:
            finish_list.append(i)

    with open('data.json', 'w', encoding='utf8') as file:
        json.dump(finish_list, file, indent=4, ensure_ascii=False)


open_file('data.csv')


