nums = [5, 7, 8, 1, 4, 2, 3]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    return arr


arr = nums.copy()
print(f"{nums} after sorting {insertion_sort(arr)}")
