pin = "1234"
attempts = 0
while attempts < 3:
    entered_pin = input('Enter PIN code: ')
    if entered_pin == pin:
        print("Payment successful!")
        break
    else:
        print('Incorrect...')
        attempts += 1
if attempts == 3:
    print('Sorry, your payment card has been blocked.')