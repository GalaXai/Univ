numbers = [2,3,2,5,8,1,9,8]
def removeDuplicats(array):
    for num in array:
        n=0
        for numi in array:
            if num==numi:
                n+=1
        if n>1:
            for i in range(n):
                array.remove(num)
    return array
print(removeDuplicats(numbers))
