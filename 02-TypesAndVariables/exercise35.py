pi = 3.14
cir = float(input('Enter tree circumference in cm: '))
diameter = cir / (2*pi)
test = diameter >= 50
print(f'Tree can be cut down: {test}')