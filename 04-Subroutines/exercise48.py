def f(product_code):
    a=0

    for i in range(0,3):
        a += int(product_code[i])

    if int(product_code[3]) == a % 7:
        return True
    else:
        return False

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
