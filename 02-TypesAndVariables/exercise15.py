####
#Converting degrees from Celsius to Kelvin and Farenheit
##

celcius_degrees = float(input("Enter a temperature in Celcius degrees: "))                  #entering temperature in Celcius degrees
kelvin_degrees = celcius_degrees + 273.15                                                   #converting celcius to kelvin
farenheit_degrees = celcius_degrees*(9/5) + 32                                              #converting celcius to farenheit
print(f'{celcius_degrees} in celcius equals to {kelvin_degrees} in kelvin and {farenheit_degrees} in farenheit')    #displaying the outcome


