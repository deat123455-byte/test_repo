import json
import csv
from datetime import datetime


def data_analysis(filename):
    with open('students.json', 'r', encoding='utf8') as file:
        data = json.load(file)
        print(len(data))
        ages = [student["возраст"] for student in data]
        max_age = max(ages)
        for i in data:
            if i["возраст"] == max_age:
                print(i["имя"])
                print(i["возраст"])
                print(i["город"])
                print(i["предметы"])
                break
        language = 0
        for r in data:
            if "Python" in r["предметы"]:
                language += 1
        print(language)


def sales_data(sales):
    with open('sales.csv', 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        total_amount = 0
        max_amount = 0
        product_with_max = ""
        sort_dict = {}
        for row in reader:
            amount = int(row["Сумма"])
            total_amount += amount
            current_amount = int(row["Сумма"])
            if current_amount > max_amount:
                max_amount = current_amount
                product_with_max = row["Продукт"]
            date = datetime.strptime(row["Дата"], "%Y-%m-%d")
            now_date = date.strftime("%Y-%m")
            if now_date in sort_dict:
                sort_dict[now_date] = sort_dict.get(now_date) + int(row["Сумма"])
            else:
                sort_dict[now_date] = int(row["Сумма"])
        print(total_amount)
        print(sort_dict)
        print(product_with_max)


def csv_json(performance):
    with open('employees.json', 'r', encoding='utf8') as file:
        data = json.load(file)
        print(data)

    with open('performance.csv', 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        combined_data = []
        for row in reader:
            for i in data:
                if i["id"] == int(row["employee_id"]):
                    combined_data.append(
                        {"имя": i["имя"], "должность": i["должность"], "performance": row["performance"]})
        print(combined_data)
        total_performance = sum(int(item["performance"]) for item in combined_data)
        average_performance = total_performance / len(combined_data)
        print(average_performance)
        performance = [average["performance"] for average in combined_data]
        performance_max = max(performance)
        for r in combined_data:
            if r["performance"] == performance_max:
                print(r["имя"])
                print(r["performance"])
                break

