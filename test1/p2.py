def f(n):
    number = 2
    result = 0
    count = 0
    while count < n:
        is_prime = True
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            result = number
            count += 1
        number += 1
    return number -1
        
print(f(8))