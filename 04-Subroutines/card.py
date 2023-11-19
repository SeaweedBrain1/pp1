def f(card_number):
    if len(card_number) != 16:
        return "Invalid card number"
    masked_number = card_number[:2] + 10*'*' + card_number[-4:]
    return masked_number
    
