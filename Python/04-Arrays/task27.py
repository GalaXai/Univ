def listToString(array):
    string_ints = [str(int) for int in array]
    string_ints = ','.join(string_ints)
    return string_ints
numbers = [5,4,3,2,6,5]
print(listToString(numbers))
print(numbers)