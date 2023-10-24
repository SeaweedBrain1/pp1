x = int(input('x: '))
y = int(input('y: '))
if x == 0 and y == 0:
    print(f'Point P({x},{y}) is at the origin of the coordinate system.')
elif x == 0:
    print(f'Point P({x},{y}) is on the y-axis.')
elif y == 0:
    print(f'Point P({x},{y}) is on the x-axis')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant.')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant.')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant.')
else:
    print(f'Point P({x},{y}) is in the fourth quadrant.')