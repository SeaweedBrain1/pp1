def f(number, even):
    string = str(number)
    suma = 0
    if even:
        for char in string:
            if int(char) % 2 == 0:
                suma += int(char)
    else:
        for char in string:
            if int(char) % 2 != 0:
                suma += int(char)

    return suma

if __name__ == "__main__":
    print(f(3124,False))

        