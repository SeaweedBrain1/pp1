import range
a = int(input('A number:'))
x = 2
y = 15
result=range.range_check(x,y,a)
if result:
    print(f'Number {a} in the range <{x},{y}>: yes')
else:
    print(f'Number {a} in the range <{x},{y}>: no')