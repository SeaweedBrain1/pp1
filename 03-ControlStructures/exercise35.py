string = ""
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        string = string + " " + "BINGO"
    elif i % 3 == 0:
        string = string + " " + "THREE"
    elif i % 5 == 0:
        string = string + " " + "FIVE"
    else:
        string = string + " " + str(i)
print(string)