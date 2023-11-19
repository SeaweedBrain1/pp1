def month(n):
    month_names = ["January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"]
    if 1 <= n <= 12:
        return month_names[n - 1]
    else:
        return "Invalid month number"

if __name__ == '__main__':
    print(month(6))