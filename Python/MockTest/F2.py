def in_range(n,begin,to):
    Flag=False
    for i in range(begin,to):
        if n==i:
            Flag=True
    return Flag