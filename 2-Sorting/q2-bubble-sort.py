nums = [5, 8, 1, 6, 2, 9, 4]


def bubble_sort(arr):
    for i in range(len(arr) - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = nums.copy()
print(f"{nums} after sorting {bubble_sort(arr)}")
