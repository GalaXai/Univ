x = int(input("Enter number: "))
y = int(input("Enter number: "))


def test(number):
    if number > 0:
        print("{} is postive ".format(number))
    elif number < 0:
        print("{} is negative".format(number))
    else:
        print("The number is = 0")


test(x)
test(y)
