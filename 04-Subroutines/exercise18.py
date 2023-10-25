def numbers(n):
    string = ''
    for i in range(1, n+1):
        string += str(i) + " "
    return(f'Numbers <1,{n}>: {string}')
print(numbers(7))
print(numbers(15))
