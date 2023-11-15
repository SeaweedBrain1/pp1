def month(n):
    month_name = ["January", "February", "March", "Apri", "May", "June", "July", "August", "September", "October", "November", "December"]
    return "Month name: " + month_name[n-1]
number = int(input("Enter month number: "))
print(month(number))