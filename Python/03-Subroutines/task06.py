def numbers_layout():
    for i in range(1, 9, +3):
        for j in range(3):
            print(" {}".format(i+j), end='')
        print()


numbers_layout()
