washing_product = "shoes"
rinse = True
spin = False
print(f'Washinf product: {washing_product}')
print(f'Rinse: {rinse}')
print(f'Spinf: {spin}')
time = 0
if washing_product == "shoes":
    time += 20
if washing_product == "jacker":
    time += 40
if washing_product == "underwear":
    time += 70
if rinse:
    time += 15
if spin:
    time += 9
print(f'Total washing time: {time}')