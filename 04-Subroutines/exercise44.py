def f(password):
    count = 0
    for char in password:
        if password.count(char) == 1:
            count += 1
    return count >= 6


print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))




