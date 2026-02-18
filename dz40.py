import json
import csv


def get_average_score():
    """Вычисляет и выводит средний балл для каждого студента."""
    with open("student_list.json", "r", encoding="utf8") as file:
        data = json.load(file)
    for student in data["students"]:
        average_score = (
            student["grades"]["math"] +
            student["grades"]["science"] +
            student["grades"]["history"]
        ) / 3
        print(f"Средний балл для студента {student['name']}: {average_score}")


def get_best_student():
    """Находит и выводит лучшего студента."""
    with open("student_list.json", "r", encoding="utf8") as file:
        data = json.load(file)
    max_score = float('-inf')
    best_student = None
    for student in data["students"]:
        average_score = (
            student["grades"]["math"] +
            student["grades"]["science"] +
            student["grades"]["history"]
        ) / 3
        if average_score > max_score:
            best_student = student["name"]
            max_score = average_score
    print(f"Наилучший студент: {best_student} (Средний балл: {max_score:.2f})")


def get_worst_student():
    """Находит и выводит худшего студента."""
    with open("student_list.json", "r", encoding="utf8") as file:
        data = json.load(file)
    min_score = float('inf')
    worst_student = None
    for student in data["students"]:
        average_score = (
            student["grades"]["math"] +
            student["grades"]["science"] +
            student["grades"]["history"]
        ) / 3
        if average_score < min_score:
            worst_student = student["name"]
            min_score = average_score
    print(f"Худший студент: {worst_student} (Средний балл: {min_score:.2f})")


def find_student(name):
    """
    Выводит информацию о студенте по имени.
    Если студент не найден, выводит сообщение об этом.
    """
    with open("student_list.json", "r", encoding="utf8") as file:
        data = json.load(file)
    for student in data["students"]:
        if student["name"] == name:
            print(f"Имя: {student['name']}")
            print(f"Возраст: {student['age']}")
            print(f"Предметы: {student['subjects']}")
            print(f"Оценки: {student['grades']}")
            return
    print("Студент с таким именем не найден")


def sort_students_by_average():
    """Сортирует и выводит студентов по среднему баллу в порядке убывания."""
    with open("student_list.json", "r", encoding="utf8") as file:
        data = json.load(file)
    list_students = []
    for student in data["students"]:
        average_score = (
            student["grades"]["math"] +
            student["grades"]["science"] +
            student["grades"]["history"]
        ) / 3
        list_students.append((student["name"], average_score))
    sorted_list = sorted(list_students, key=lambda x: x[1], reverse=True)
    print("Сортировка студентов по среднему баллу:")
    for name, score in sorted_list:
        print(f"{name}: {score:.2f}")


def new_list():
    """Преобразует данные в новый формат и выводит результат."""
    with open("student_list.json", "r", encoding="utf8") as file:
        data = json.load(file)
    students = []
    for student in data["students"]:
        student_dict = {
            "name": student["name"],
            "age": student["age"],
            "subjects": student["subjects"],
            "grades": student["grades"]
        }
        students.append(student_dict)
    print(students)


def save_students_to_csv():
    """Сохраняет данные о студентах в CSV-файл."""
    with open("student_list.json", "r", encoding="utf8") as file:
        data = json.load(file)
    csv_file = []
    for student in data["students"]:
        average_score = (
            student["grades"]["math"] +
            student["grades"]["science"] +
            student["grades"]["history"]
        ) / 3
        average_score = round(average_score, 1)
        csv_file.append([student["name"], student["age"], average_score])

    with open("student_list.csv", "w", encoding="utf8") as new_file:
        writer = csv.writer(new_file, delimiter=' ')
        for row in csv_file:
            writer.writerow(row)


if __name__ == "__main__":
    get_average_score()
    print()
    get_best_student()
    get_worst_student()
    print()
    find_student("John")
    print()
    sort_students_by_average()
    print()
    new_list()
    print()
    save_students_to_csv()