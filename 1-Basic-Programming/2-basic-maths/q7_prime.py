# loop till n or n//2 to check which is divisible = O(N)
# below is the optimal solution = O(sqrt(N))

num = int(input("Give a number: "))
factors = []

for i in range(2, int((num**0.5) + 1)):  # O(sqrt(N))
    if num % i == 0:
        factors.append(i)  # O(1)

if len(factors) == 0:  # O(1)
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
