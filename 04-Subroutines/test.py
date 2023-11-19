def f(dice):
    count = 0
    number = dice[0]
    maximum = 0
    result = ""
    for char in dice:
        if char == number:
            count += 1
        else:
            if count > maximum:
                maximum = count
                result = number
            count = 1
        number = char
    if count > maximum:
        result = number

    return result

print(f("12333333332333444455555"))

