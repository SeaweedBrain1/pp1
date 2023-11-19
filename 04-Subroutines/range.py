def range_check(left_border, right_border, value):
    return left_border <= value <= right_border
if __name__ == "__main__":
    a = range_check(2,5,7)
    print(a)
