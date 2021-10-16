print("Enter a and b")
a = int(input())
b = int(input())
print("* "*b)
for i in range(a-2):
    print("*" + " " * (2*b-3) + "*")
print("* "*b)
