# Алгоритм проверки наличия дубликатов в массиве.
def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False
# Тут будет сложность  O(n^2), так как нужно пройтись по каждому элементу массива. В практических условиях можно использовать на небольших массивах, чтобы быстро проверить на дубликаты.
# Чем больше n, тем сильнее возрастает время выполнения.


# Алгоритм поиска максимального элемента в неотсортированном массиве.
def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val
# Тут будет сложность О(n). Цикл проходит по массиву 1 раз. Нет вложенных циклов.
# Время выполнения зависит от n. Встроенная функция max() более оптимизированная.

# Алгоритм сортировки выбором (Selection Sort).
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
# Тут сложность O(n^2) в худшем и среднем случае. Так как мы опять же проходим по всем элементам и число шагов увеличивается от длины массива. Также можем использовать в небольших массивах данных.


# Алгоритм быстрой сортировки (Quick Sort).
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Тут сложность O(n log n) в среднем и в худшем случае O(n^2). Можно сортировать уже средние массивы данных. Выбор опорного элемента может привести к O(n^2).


# Алгоритм вычисления n-го числа Фибоначчи (рекурсивно).
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# Тут будет сложность O(2^n) потому что рекурсивная функция вызывает себя дважды на каждом шаге, что приводит к экспоненциальному росту числа вызовов.
# На практике можно использовать, если число n будет небольшим.