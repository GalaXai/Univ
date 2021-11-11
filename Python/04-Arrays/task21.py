def secondLargest(array):
    array.sort()
    for i in range (1,len(array)+1):
        if array[-i-1] != array[-i]:
            return array[-i-1]
numbers = [5,1,9,6,1]
print(secondLargest(numbers))
#test
test = [1,3,9,9,9,9,9,7,9,9,9,9,9,9,9,9,9]
print(secondLargest(test))