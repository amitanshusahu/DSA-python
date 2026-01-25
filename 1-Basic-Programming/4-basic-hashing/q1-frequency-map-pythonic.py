arr = [1, 2, 3, 4, 5, 1, 2, 5, 5, 5]

freq_map = {}

# the get method in a dict finds a key if not present returns given default value
for i in range(0, len(arr)):
    freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1

print(freq_map)
