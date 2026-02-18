def selection_sort(arr):
    g = len(arr)
    for i in range(g):
        min_idx = i
        for j in range(i + 1, g):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)
