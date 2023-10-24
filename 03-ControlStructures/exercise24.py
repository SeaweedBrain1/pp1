price = 200
discount_price = 140
print(f'Current product price: {discount_price}')
print(f'Previous product price: {price}')
discount = (price - discount_price) / price
if discount >= 0.1:
    print(f'Buy the product!!\nProduct price reduced by {discount*100}%')