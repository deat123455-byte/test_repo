def main():
    # Задание 1: Сортировка словаря учеников по возрасту
    students_dict = {
        'Саша': 27,
        'Кирилл': 52,
        'Маша': 14,
        'Петя': 36,
        'Оля': 43,
    }

    sorted_students_dict = sorted(students_dict, key=lambda student: students_dict[student])
    print("Отсортированные по возрасту:", sorted_students_dict)

    # Задание 2: Сортировка по индексу массы тела
    data = [
        (82, 191),
        (68, 174),
        (90, 189),
        (73, 179),
        (76, 184)
    ]

    sorted_data = sorted(data, key=lambda x: x[0] / ((x[1] / 100) ** 2))
    print("Отсортированные по ИМТ:", sorted_data)

    # Задание 3: Найти ученика с минимальным возрастом
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    min_age_student = min(students_list, key=lambda min_age: min_age["age"])
    print("Минимальный возраст:", min_age_student)


if __name__ == "__main__":
    main()