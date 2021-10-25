numbers = [12,6,4,9,3]
def star(n):
    print("{}:".format(n),('* ')*n)

def ListOfStars(array):
    for num in array:
        star(num)

ListOfStars(numbers)