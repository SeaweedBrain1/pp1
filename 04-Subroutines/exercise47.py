def f(text):
    if len(text) >= 1:
        string = ""
        string += text[0]
        for i in range(1, len(text)):
            string += "-" + text[i]
        return string
    else:
        return ""

print(f("University"))
print(f("UE"))
print(f("x"))
print(f(""))