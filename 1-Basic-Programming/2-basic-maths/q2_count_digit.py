n = 12345
num = n
count = 0

while num > 0:  # O(k), k is the num of digits
    last_digit = num % 10
    num = num // 10
    count = count + 1

print(f"There are {count} digits")
