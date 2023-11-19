def f(dice):
    number = dice[0]
    count = 0
    maximum = 0
    result = 0
    for char in dice:
        if char == number:
            count +=1
        else:
            if count > maximum:
                maximum = count
                result = int(number)
            count = 1
        number = char
    if count > maximum:
        result = int(number)

    return result

print(f('11111111111523333165554211222222'))
print(f("11212"))


