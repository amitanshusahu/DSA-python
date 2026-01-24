# tail recurssion : recursive fuction call is done at the end. no job after recurssive function call
def fun(x, n):
    if n == 0:
        return
    print(x)
    fun(x, n - 1)


fun("godslayer", 5)  # O(n)
