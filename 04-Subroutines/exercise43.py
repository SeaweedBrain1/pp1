def f(name):
    string = ""
    string += name[0]
    add = False
    for char in name:
        if add:
            string += char
        add = False
        if char == " ":
            add = True
    return string

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))
