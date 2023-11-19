def numbers(n):
    string = ''
    for i in range(1, n):
        string += str(i) + " "
    string += str(i+1)
    return(f'Numbers <1,{n}>: {string}')
print(numbers(7))
print(numbers(15))
