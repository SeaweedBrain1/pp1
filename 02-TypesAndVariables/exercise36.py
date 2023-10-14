buying = float(input('Bank buys EUR: '))
selling = float(input('Bank sells EUR: '))
spread = round(selling - buying, 4)
print(f'Spread: {spread}')