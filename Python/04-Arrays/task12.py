numbers = [15,8,31,47,2,19]
numbers.reverse()
print(numbers)
#OR
def rev_num(list):
    rev = []
    for num in list:
        rev.insert(0,num)
    return rev
numbers = [15,8,31,47,2,19]
print(rev_num(numbers))