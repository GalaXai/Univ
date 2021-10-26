def LargestandSmallest(array):
    array.sort()
    return array[-1] - array [0]
print(LargestandSmallest([1,0,9,4,6]))
print(LargestandSmallest([6,8,3,1,0,5,7]))