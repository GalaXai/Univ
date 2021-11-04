def dectobin(n):
    binary=""
    while n>0:
        if n == 1:
            binary+="1"
            binary+="0"
            break
        if n / 2 == n//2:
            binary+="0"
        else:
            binary+="1"
        n=n//2
    return int(binary)