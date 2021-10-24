def piramid(n):
    if n >= 0:
        for i in range(n+1):
            print("* " * i)
            n -= 1
        i -= 1
        for x in range(i):
            print("* " * i)
            i -= 1


print("Enter the number")
x = int(input())
piramid(x)
