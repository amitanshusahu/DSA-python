num = 1234

while num > 0:  # O(k), k is the num of digits
    last_digit = num % 10
    num = num // 10
    print(last_digit)
