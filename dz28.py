import csv
from os import write


with open('prices.txt', 'r', encoding='utf8') as f:
    data = f.read().splitlines()


with open('prices.csv', 'w', encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in data:
        data_one = i.split('\t')
        writer.writerow(data_one)


def average_cost():
    with open('prices.csv', 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        total_cost = 0
        for r in reader:
            cost = int(r[1]) * int(r[2])
            total_cost += cost
        return total_cost

print(average_cost())
