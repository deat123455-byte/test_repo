from functools import reduce


def cubes_of_numbers(number):
    """Возвращает куб числа."""
    return number ** 3


def is_divisible_by_five(number):
    """Проверяет, делится ли число на 5."""
    return number % 5 == 0


def is_odd(number):
    """Проверяет, является ли число нечётным."""
    return number % 2 != 0


def multiply(x, y):
    """Возвращает произведение двух чисел."""
    return x * y


def main():
    # Задание 1: Кубы чисел
    list_of_numbers_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cubes = list(map(cubes_of_numbers, list_of_numbers_one))
    print("Кубы:", cubes)

    # Задание 2: Числа, делящиеся на 5
    list_of_numbers_two = [3, 4, 5, 8, 10, 14, 15, 19, 20]
    filtered_numbers = list(filter(is_divisible_by_five, list_of_numbers_two))
    print("Делятся на 5:", filtered_numbers)

    # Задание 3: Произведение нечётных чисел
    list_odd_number = [23, 8, 15, 42, 17, 9, 34, 11, 6, 29]
    filter_odd_number = list(filter(is_odd, list_odd_number))
    the_product_odd_of_numbers = reduce(multiply, filter_odd_number)
    print("Произведение нечётных:", the_product_odd_of_numbers)


if __name__ == "__main__":
    main()