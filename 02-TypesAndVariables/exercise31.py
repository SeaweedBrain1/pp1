import random
num = random.randint(1, 6)
user_num = int(input('Enter a number between 1 and 6: '))
test = num == user_num
print(f'Numbered guessed: {test}\nThe number was: {num}')