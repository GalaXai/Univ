def f4(d):
    #d == dict
    output = 0
    numbers = [5,6,7,8,9,10]
    x = d.values()
    print(type(x))
    for i in x:
        for z in i:
            for x in numbers:
                if z == x:
                    output+=int(z)
                    break
    return output
print(f4({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}))