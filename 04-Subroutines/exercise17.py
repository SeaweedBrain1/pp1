def different(n1, n2, n3):
    return(n1 != n2 and n1 != n3 and n2 != n3)
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))
print(different(first_number, second_number, third_number))