def sum(array):
    sum_V = 0
    for x in range(len(array)):
        sum_V += array[x]
    return sum_V
def arr2str(array):
    string_ints = [str(int) for int in array]
    string_ints = ','.join(string_ints)
    return string_ints
array = [4,3,7,1,3]
print(sum(array))
print(arr2str(array))
print(array)



'''
for int in array:
    str(int)
#################
[str(int) for int in array]
'''
