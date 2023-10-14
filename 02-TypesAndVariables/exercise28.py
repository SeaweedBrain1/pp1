height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))
bmi = round(weight / (height / 100)**2, 2)
correct_weight = bmi >= 18.5 and bmi <= 24.9
print(f'Your BMI index: {bmi}')
print(f'Correct weight: {correct_weight}')