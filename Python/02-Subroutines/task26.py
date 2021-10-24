correct = "0805"
attempt = 3
while attempt > 0:
    print("Enter the PIN code")
    pin = input()
    if pin == correct:
        print("Access granted!")
        break
    else:
        print("Incorrect pin")
    attempt -= 1
if attempt == 0:
    print("Sorry, your payment card has been blocked")
