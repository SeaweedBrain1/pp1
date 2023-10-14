height_cm = 183                                     #declaration of your height
height_inches = height_cm / 2.54                    #transforming height to inches
feet = height_inches // 12                          #finding how many feet is in the inches
remainder_inches = height_inches % 12               #finding reminder of the inches
print(f'I am {height_cm}cm tall, i.e. {feet} feet and {round(remainder_inches)} inches')
