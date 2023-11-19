def read_number():
    number = int(input('Enter a number: '))
    return(number)
if __name__ == "__main__":
    a = read_number()
    b = read_number()
    print(f'{a} + {b} = {a+b}')