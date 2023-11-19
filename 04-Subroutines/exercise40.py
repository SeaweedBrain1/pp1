
def f(number):
    result = 0
    string = str(number)
    for i in range(1,10):
        count = 0
        x = 0
        for char in string:
            if str(i) == char:
                count += 1
                x += int(char)
        if count < 2:
            pass
        else:
            result += x
    return result

print(f(1027))
print(f(230335))
print(f(513553007))







