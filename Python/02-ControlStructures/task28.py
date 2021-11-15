x = 0
y = 1
n = 5
print(x)
print(y)
for i in range(n-2):
    if n>=3:
        if i % 2 == 0:
            print(x+y)
            x=x+y
        if i % 2 == 1:
            print(x+y)
            y=x+y
    elif n==1:
        print(1)
    elif n==0:
        print(0)
#^^^ print all numbers
#vvv print #n number of fibonacci sequance
def Fibonacci(n):
    x = 0
    y = 1
    for i in range(n-3):
        if n>=3:
            if i % 2 == 0:
                x=x+y
            if i % 2 == 1:
                y=x+y
        elif n==1:
             return 1
        elif n==0:
           return 0
    return x+y
#print(Fibonacci(6))