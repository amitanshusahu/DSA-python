# given a number print it's factors/divisors (nums that are divisivle by input)
# loop till n or n//2 to check which is divisible = O(N)
# below is the optimal solution = O(sqrt(N))

n = int(input("Give a number: "))
result = []

for i in range(1, int((n**0.5) + 1)):  # O(sqrt(N))
    if n % i == 0:
        result.append(i)  # O(1)
    if n // i != i:
        result.append(n // i)  # O(1)

print(f"the factors of {n} are: ", result)
