dec = int(input('Enter a decmial number: '))
dec_end = dec
bin_number = ""
while dec != 0:
    remainder = dec % 2
    bin_number = str(remainder) + bin_number
    dec = dec // 2
print(f'{dec_end}(10) = {bin_number}(2)')

    