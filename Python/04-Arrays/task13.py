def secondPower(*args):
    number_1 = [*args]
    number_2 = []
    for num in number_1:
        number_2.append(num**2)
    print(number_2)
secondPower(15,8,31,47,2,19)
secondPower(8,2,5,1,9)