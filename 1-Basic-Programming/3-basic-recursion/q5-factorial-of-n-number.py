def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # TC -> O(n) n calls, SC -> O(k) , k is stack space
