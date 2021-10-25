numbers_1 = [4,36,12,28,9,44,5]
numbers_2 = [5,1,36]
def removeDuplication(array1,array2):
     for num in array1:
         for int in array2:
             if num == int:
                 array1.remove(num)
     return array1

print(removeDuplication(numbers_1,numbers_2))