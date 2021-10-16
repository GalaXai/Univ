
n = 1
i = 0
sum = 0
while n != 0:
    print("Enter number ")
    n = int(input())
    if n == 0:
        break
    i += 1
    sum += n
if i == 0:
    mean = 0
else:
    mean = sum / i
print("Result: Quantity {} ,Sum = {}, Mean= {}".format(i, sum, mean))
