def comparee(array1,array2):
    if len(array1)==len(array2):
        for x in range(len(array1)):
            Flag = array1[x] == array2[x]
    else:
        Flag = False
    print("Array 1 :",array1)
    print("Array 2 :",array2)
    if Flag == True:
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")  
    return Flag

print(comparee(["water","book","sky"],["water","book","sky"]))
print(comparee([True,False],[True,False,True]))
print(comparee([5,3,1],[5,3,1]))
print(comparee([3,2,1],[3,2]))