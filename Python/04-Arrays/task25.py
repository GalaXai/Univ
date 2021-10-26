def minmax(array):
    Result = []
    Result.append(min(array))
    Result.append(max(array))
    return min(array),max(array),Result
numbers = [4,2,8,4,7,9,5]
print(minmax(numbers))