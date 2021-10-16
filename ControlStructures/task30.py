num = 0


def prime_check(num):
    flag = False
    if num <= 1:
        return 0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

    if flag:
        pass
    else:
        print(num, "is a prime number")


for x in range(20):
    prime_check(x)
