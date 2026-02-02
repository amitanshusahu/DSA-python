def merge_two_sorted_arr(left_arr, right_arr):
    result = []
    i = j = 0
    left_arr_len = len(left_arr)
    right_arr_len = len(right_arr)
    while i < left_arr_len and j < right_arr_len:
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    if i < left_arr_len:
        while i < left_arr_len:
            result.append(left_arr[i])
            i += 1
    if j < right_arr_len:
        while j < right_arr_len:
            result.append(right_arr[j])
            j += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)
    return merge_two_sorted_arr(left_sorted, right_sorted)


arr = [9, 6, 2, 1, 7, 8]
print(merge_sort(arr))
