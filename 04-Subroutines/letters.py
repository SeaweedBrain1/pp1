def letter_counter(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count