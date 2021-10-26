import random
def rand_elem(array):
    return array[random.randrange(len(array))]
numbers = [8,12,78,69,13,18,1,0,9,7]
for i in range(random.randrange(10)):
    print(rand_elem(numbers))
