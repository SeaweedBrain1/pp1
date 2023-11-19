def f(a,b):
    string = ""
    if a > b:
        c = a - b
        string += str(a) + "-" + str(b) + "=" + str(a-b)
    if a <= b:
        c = a + b
        string = str(a) + "+" + str(b) + "=" + str(a+b)
    return string

print(f(20,8))
print(f(8,12))
print(f(7,7))