number = int(input('Enter a number: '))
if number >= 0:
    print(f'|{number}| = {number}')
else:
    print(f'|{number}| = {-number}')
print(abs(number))