def numbers_layout():
    i = 0
    j = 0
    for i in range(1, 9, +3):
        for j in range(3):
            print(" {}".format(i+j), end='')
        print()


numbers_layout()
