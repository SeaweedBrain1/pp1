import mymath, mykeybord
a = mykeybord.read_number()
b = mymath.generate_number()
print(f'Computer number: {b}')
if a == b:
    print('You won the game!')
else:
    print('You did not win the game...')