def NumbersInList(*args):
    numbers = [*args]
    odd = 0
    even = 0
    for x in range(len(numbers)):
        if numbers[x] % 2 == 0:
            even +=1
        else:
            odd +=1
    print("Ammount of odd numbers : {}".format(odd))
    print("Ammount of even numbers : {}".format(even))
    return 0

NumbersInList(5,3,2,1,5,1,23,4,1,6,12,7,3,132,4,123,421,321,1)