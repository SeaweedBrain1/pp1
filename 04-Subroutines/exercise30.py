def f(number, even):
    sum_of_digits = 0
    str_number = str(number)
    if even:
        for char in str_number:
            if int(char) % 2 == 0:
                sum_of_digits += int(char)
        return sum_of_digits
    else:
        for char in str_number:
            if int(char) % 2 != 0:
                sum_of_digits += int(char)
        return sum_of_digits
if __name__ == "__main__":
    print(f(3124,True)) 
    print(f(3124,False)) 
    print(f(20576,False)) 
    print(f(20576,True)) 
    print(f(13115,True)) 
 




