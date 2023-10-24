number = int(input('Number of products purchased: '))
price = int(input('Product price: '))
if number <= 2:
    pay = number * price
else:
    pay = 2*price + (number-2)*(0.75*price)
print(f'Amount to pay: {pay}')