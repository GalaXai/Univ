#""" as stack = list
def dectobin(n):
    binary=[]
    while n>0:
        if n==0:
            binary.append(0)
            break
            n-=1
        if n / 2 == n//2:
            binary.append(0)
        else:
            binary.append(1)
        n=n//2
    binary.reverse()
    return binary
print(dectobin(20))
#"""