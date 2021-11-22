#vvv print sum of fibonacci numbers
def Fibonacci(n):
    if n <= 1:
       return n
    return (Fibonacci(n-1) + Fibonacci(n-2))

x=10
print(Fibonacci(x-1))
