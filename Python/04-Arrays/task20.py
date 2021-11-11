def occour(number,array):
    flag = False
    for num in array:
        if number ==  num:
            flag = True
            break
    if flag == True:
        return print("Result: number {} appears in the array".format(number))
    else:
        return print("Result: number {} doesn't appears in the array".format(number))
numbers = [15,38,7,23,14]
occour(23,numbers)
occour(24,numbers)