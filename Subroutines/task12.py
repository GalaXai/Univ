def sum(n):
    if n == 1:
        return 1
    if n > 1:
        return n + sum(n-1)

n = int(input())
print(" Sum of numbers in range of {} is equal to {}".format(n,sum(n)))