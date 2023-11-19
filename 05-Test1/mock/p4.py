def f(card_number):
    masked_number = ""
    masked_number += card_number[:2]
    masked_number += 10*"*"
    masked_number += card_number[-4:]
    return masked_number

if __name__ == "__main__":
    print(f("5290312400019022"))