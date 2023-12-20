distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

def avg_speed(distance, hours, minutes):
    return round(distance/(hours+(minutes/60)), 1)

print(avg_speed(distance, hours, minutes))