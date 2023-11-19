def f(detector):
    count = 0
    for char in detector:
        if char == "+":
            count += 1
        if char == "-":
            count -= 1
        if count == 3:
            return True
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
