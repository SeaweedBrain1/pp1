a = float(input("Enter first side of the triangle: "))
b = float(input("Enter second side of the triangl: "))
c = float(input("Enter third side of the triangle: "))                        #enetering values of 3 sides of a triangle
p = (a + b + c ) / 2                                                          #calculating half of the circumference of the triangle
area = (p*(p-a)*(p-b)*(p-c))**(1/2)
print(f'Triangle area: {area}')
print(f'Triangle circumference: {p*2}')
