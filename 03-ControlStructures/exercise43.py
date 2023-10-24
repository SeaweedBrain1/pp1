first = 0
second = 1
string = "0 1"
for i in range(3, 21):
    next = first + second
    string += " " + str(next)
    first = second
    second = next
print(string)


    