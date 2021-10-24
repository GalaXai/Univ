
n = 1
i = 0
sum = 0
while n != 0:
    n = int(input("Enter number: "))
    if n == 0:
        break
    i += 1
    sum += n
if i == 0:
    mean = 0
else:
    mean = sum / i
print("Result: Quantity {} ,Sum = {}, Mean= {}".format(i, sum, mean))
