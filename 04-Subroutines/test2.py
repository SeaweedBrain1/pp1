def f(n):
    count = 0
    number = 2
    is_prime = True
    while count < n:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            count +=1
        number += 1
    return number - 1

print(f(1))

