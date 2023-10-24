time24 = input('Enter time (24-hour format, hh:mm): ')
hours, minutes = map(int, time24.split(':'))
if hours >= 12:
    end = "pm"
    hours -= 12
else:
    end = "am"
print(f'Time is {hours}:{minutes} {end}')
