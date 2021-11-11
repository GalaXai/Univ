def secondPower(*args):
    number1 = [*args]
    number2 = []
    for num in number1:
        number2.append(num**2)
    return number2
print(secondPower(15,8,31,47,2,19))
print(secondPower(8,2,5,1,9))