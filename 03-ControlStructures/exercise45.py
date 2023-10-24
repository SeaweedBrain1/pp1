N = int(input("Enter the value of N: "))
print(f"The first {N} prime numbers are:")
num = 2
count = 0
while count < N:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
        count += 1
    num += 1

    
    