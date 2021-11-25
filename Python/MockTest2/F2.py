def f2(a1,a2):
    out_1 = 0
    out_2 =0
    for i in a1:
        if len(str(i)) == 2:
            out_1+=1
    for x in a2:
        if len(str(x)) == 2:
            out_2+=1
    if out_1 == out_2:
        return True
    else:
        return False
print(f2([23,7,16,34],[1,18,79,20,6,111]))
