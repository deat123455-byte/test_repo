def main():
    # Задание 1: Оставить строки длиной больше 4
    fruits = ["apple", "kiwi", "banana", "fig"]
    filtered_fruits = list(filter(lambda fruit: len(fruit) > 4, fruits))
    print("Фильтр по длине:", filtered_fruits)

    # Задание 2: Найти студента с максимальной оценкой
    students = [
        {"name": "John", "grade": 90},
        {"name": "Jane", "grade": 85},
        {"name": "Dave", "grade": 92}
    ]
    best_student = max(students, key=lambda student: student["grade"])
    print("Лучший студент:", best_student)

    # Задание 3: Сортировка кортежей по сумме
    tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
    sorted_tuples = sorted(tuples, key=lambda x: x[0] + x[1])
    print("Отсортированные кортежи:", sorted_tuples)

    # Задание 4: Оставить только чётные числа
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = list(filter(lambda y: y % 2 == 0, numbers))
    print("Чётные числа:", even_numbers)

    # Задание 5: Сортировка объектов Person по возрасту
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"Person(name='{self.name}', age={self.age})"

    people = [
        Person("John", 24),
        Person("Jane", 31),
        Person("Dave", 22)
    ]
    sorted_people = sorted(people, key=lambda person: person.age)
    print("Отсортированные люди:", sorted_people)


if __name__ == "__main__":
    main()