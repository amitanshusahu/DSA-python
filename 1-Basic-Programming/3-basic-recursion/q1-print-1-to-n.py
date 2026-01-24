# head recursion - job is done after recursive function call, i.e the function call is in the head and not tail
def func(n):
    if n == 0:
        return
    func(n - 1)
    print(n)


func(2)
