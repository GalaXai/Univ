def BubbleSort(array):
    for i in array:
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
   
numbers = [4,3,5,1,2]
print(BubbleSort(numbers))
