a = 4
b = 15
print(f'a = {a} and b = {b}')
for i in range(1, (a+1)):
    if i == 1 or i == a:
        print(b * "*")
    else:
        print("*" + (b-2) * " " + "*")