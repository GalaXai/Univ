def AmmountGratherThan(number,array):
    ammount = 0
    for num in array:
        if number < num:
            ammount +=1
    return ammount
print(AmmountGratherThan(3,[1,2,3,4,6,7,4,54,6]))
