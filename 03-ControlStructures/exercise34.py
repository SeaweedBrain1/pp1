amount_of_money = int(input('Enter the amount in PLN: '))
pln_5 = amount_of_money // 5
remainder = amount_of_money % 5
pln_2 = remainder // 2
remainder2 = remainder % 2
pln_1 = remainder2
print(f'The amount of PLN {amount_of_money} in coins: \n5 zl: {pln_5}\n2 zl: {pln_2}\n1 zl: {pln_1} ')