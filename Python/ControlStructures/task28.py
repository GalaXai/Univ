x = 0
y = 1
n = 15
print(x)
print(y)
for z in range(n):
    print(x+y)
    x += y
    print(y+x)
    y += x
