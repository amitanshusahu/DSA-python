n = 12345
num = n

reverse_num = 0

while num > 0:  # O(k), k is the num of digits
    last_digit = num % 10
    num = num // 10
    reverse_num = (reverse_num * 10) + last_digit

if n != reverse_num:
    print(f"The given number {n} is not palindrome")
else:
    print(f"The given number {n} is palindrome")
