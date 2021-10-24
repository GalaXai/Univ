a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("* "*b)
for i in range(a-2):
    print("*" + " " * (2*b-3) + "*")
print("* "*b)
