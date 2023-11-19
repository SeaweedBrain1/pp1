def f(p):
    result = 0
    for char in p:
        count = p.count(char)
        if count < 2:
            result += 1
        else:
            return False
    return result >= 6

print(f("a12345678"))

    
        

