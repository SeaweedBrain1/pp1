def pay(hours, rate):
    try:    
        if hours >= 40:
            pay = 40*rate + (hours-40)*1.5*rate
        else:
            pay = rate * hours
        return(pay)
    except:
        return("Error, enter numeric input")

print(pay(45, 10))