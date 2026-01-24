n = 12345
num = n
reverse_number = 0

while num > 0:
    last_digit = num % 10
    num = num // 10
    reverse_number = (reverse_number * 10) + last_digit

print(f"The reverse of given number {n} is {reverse_number}")
