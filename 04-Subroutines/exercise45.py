def f(expression):
    current_number = 0
    result = 0
    current_operator = '+'

    for char in expression:
        if char.isdigit():
            current_number = int(char)
        elif current_operator == '+':
                result += current_number              
                current_operator = char
        elif current_operator == '-':
                result -= current_number
                current_operator = char

    if current_operator == '+':
        result += current_number
    elif current_operator == '-':
        result -= current_number

    return result

print(f("2+3"))      # Output: 5
print(f("3+8+1"))    # Output: 12
print(f("2+3-4+5-0")) # Output: 6