def f(w):
    if w == "":
        return ""
    string = w[0]
    for i in range(1, len(w)):
        if i % 2 != 0:
            string += "+" + w[i]
        elif i % 2 == 0:
            string += "-" + w[i]
    return string

print(f("k"))



