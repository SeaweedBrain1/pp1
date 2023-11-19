
def f(n):
    first = 0
    second = 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        for i in range(1, n-1):
            a = second
            second = first + a
            first = a
        return(second)
    
print(f(5))
print(f(9))


