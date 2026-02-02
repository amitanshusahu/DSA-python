def partition(arr, low, high):
    p = low
    i = low
    j = high
    while i < j:
        while arr[i] <= arr[p] and i < high:
            i += 1
        while arr[j] > arr[p] and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[p], arr[j] = arr[j], arr[p]
    return j


def quick_sort(arr, low, high):
    if low >= high:
        return
    partition_index = partition(arr, low, high)
    quick_sort(arr, 0, partition_index - 1)
    quick_sort(arr, partition_index + 1, high - 1)


arr = [4, 1, 2, 3, 7, 6, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
