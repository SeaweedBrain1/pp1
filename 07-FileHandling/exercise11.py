file = open('numbers.txt','r')
counter = 0
for line in file:
     counter += int(line)
     print(line.rstrip(), end=" ")
print()
print(f'Sum: {counter}')
file.close()