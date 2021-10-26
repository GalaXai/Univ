def subset(array1,array2):
    flag = False
    for num in array1:
        for numi in array2:
            if num == numi:
                flag = True
                break
            else:
                flag=False
        if flag == False:
            return False
    return flag
            
numbers = [1,2,3]
numbers2 = [1,2,3,4]
print(subset(numbers,numbers2))
