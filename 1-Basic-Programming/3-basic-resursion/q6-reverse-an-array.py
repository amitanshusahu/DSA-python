def reverse_arr(arr, left_pointer, right_pointer):
    if right_pointer <= left_pointer:
        return arr
    arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
    return reverse_arr(arr, left_pointer + 1, right_pointer - 1)


print(reverse_arr([1, 2, 3, 4], 0, 3))
