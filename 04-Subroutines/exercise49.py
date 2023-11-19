def f(dice): 
    number = ""
    string = ""
    maximum = 0
    result = 0
    count = 0
    for char in dice:
        if char != number:
            string += " "
        string += char
        number = char
    for i in string:
        if i == " ":
            if count > maximum:
                maximum = count
                result = remember
            count = 0
        else:
            count +=1
            remember = i
    if count > maximum:
        result = remember

    return result

        


print(f("1113333333311112222122"))
print(f("22213313131313"))


