numbers = [15,8,31,47,2,19]
numbers.reverse()
print(numbers)
#OR
numbers = [15,8,31,47,2,19]
rev_num = []
for num in numbers:
    rev_num.insert(0,num)
    print(num)
print(rev_num)