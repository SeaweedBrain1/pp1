def f(binary_number):
    count = 0
    for char in binary_number:
        if char == "1" or char == "0":
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    print(f("101010a11010101"))