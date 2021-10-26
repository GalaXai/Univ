numbers = [1,23,5,282,1,17,4,906]
def numbersInAbBox(arrays):
    for i in range(len(arrays)*5):
        print("-",end='')
    print()
    for num in arrays:
        print('|',num,end='')
    print('|')
    for i in range(len(arrays)*5):
        print("-",end='')
    #-
numbersInAbBox(numbers)