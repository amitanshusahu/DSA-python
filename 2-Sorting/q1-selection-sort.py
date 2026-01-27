nums = [5, 7, 8, 1, 4, 2, 3]


def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = nums.copy()
print(f"{nums} after selection sort {selection_sort(arr)}")
