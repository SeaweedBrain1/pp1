def f(name):
    string = name[0]
    i = 0
    for char in name:
        if char == " ":
            string += name[i + 1]
        i += 1
    return string
if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))

