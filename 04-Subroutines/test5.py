def f(expression):
    current_operator = "+"
    number = 0
    result = 0
    for char in expression:
        if current_operator == "+":
            result += number
            current_operator = char
        elif current_operator == "-":
            result -= number
            current_operator = char
        else:
            number = int(char)
    if current_operator == "+":
        result += number
    elif current_operator == "-":
        result -= number
    return result

print(f("2+3-7"))
        


