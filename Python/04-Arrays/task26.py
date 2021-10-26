def OddANDEven(array):
    Odd = []
    Even = []
    for num in array:
        if num %2 == 0:
            Even.append(num)
        else:
            Odd.append(num)
    return Odd,Even
print(OddANDEven([6,8,3,1,0,5,7]))