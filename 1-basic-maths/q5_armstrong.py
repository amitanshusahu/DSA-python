n = 1634
num = n

sum = 0
count = 0

while num > 0:
    digit = num % 10
    num = num // 10
    count += 1

num = n

while num > 0:
    digit = num % 10
    num = num // 10
    sum = sum + digit**count

if sum == n:
    print(f"The given number {n} is a armstrong number")
else:
    print(f"The given number {n} is not a armstrong number")
