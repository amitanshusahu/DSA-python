arr = [1, 2, 3, 4, 5, 1, 2, 5, 5, 5]

freq_map = {}

for i in range(0, len(arr)):
    if arr[i] in freq_map:
        freq_map[arr[i]] += 1
    else:
        freq_map[arr[i]] = 1


print(freq_map)
