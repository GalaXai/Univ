numbers = [1,23,5,282,1,17,4,906]
def numbersInAbBox(arrays):
    for i in range(len(arrays)*5):
        print("-",end='')
    print()
    for num in arrays:
        x = 3-len(str(num))
        print('|'+' '*x,num,end='')
    print('|')
    for i in range(len(arrays)*5):
        print("-",end='')
numbersInAbBox(numbers)