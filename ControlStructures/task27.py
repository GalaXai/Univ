
for i in range(6, -1, -3):
    for j in range(1, 4):
        print(" {}".format(i+j), end='')
    print()
i = 6
print("#################################")
while i >= 0:
    j = 1
    while j <= 3:
        print(" {}".format(i+j), end='')
        j += 1
    i -= 3
    print()
