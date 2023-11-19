def f(sentence):
    string = ""
    for char in sentence:
        if char == " ":
            pass
        else:
            string += char
    return string

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))