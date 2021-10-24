x = int(input("Enter number: "))
y = int(input("Enter number: "))

if x > 0:
    if y > 0:
        print("Point P({},{}) is in the first quadrant of the coordinate system".format(
            x, y))
    else:
        print("Point P({},{}) is in the forth quadrant of the coordinate system".format(
            x, y))
elif y > 0:
    print("Point P({},{}) is in the second quadrant of the coordinate system".format(
        x, y))
else:
    print("Point P({},{}) is in the third quadrant of the coordinate system".format(
        x, y))
