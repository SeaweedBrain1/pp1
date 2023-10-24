sum_of_numbers = 0
count = 0
while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    sum_of_numbers += number
    count += 1
if count == 0:
    mean = 0
else:
    mean = sum_of_numbers / count
print(f"RESULT: Quantity={count}, Sum={sum_of_numbers}, Mean={mean}")