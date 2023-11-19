def f(binary_number):
    count = 0
    for char in binary_number:
        if char != "0" and char != "1":
            count += 1
    return count == 0
