def f1(a):
    output = 0
    # a =array
    for i in a:
        if i>8 and i % 2==0:
            output +=1
    return output

print(f1([13,7,4,16,3,12,8]))