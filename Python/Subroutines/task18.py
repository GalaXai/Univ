def sumOfDigits(number):
    wynik = 0
    for i in str(number):
        wynik += int(i)
    return wynik


print(sumOfDigits(7182))
