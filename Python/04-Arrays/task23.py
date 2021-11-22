def median(array):
    array.sort() #uporządkowanym
    x = len(array)
    if x%2 == 0:
        x = int(x/2)
        return (array[x-1] + array[x]) /2
    else:
        return array[int(x/2)]
print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))
print(median([1,2,3,4,5,6]))
print(median([1,2]))
