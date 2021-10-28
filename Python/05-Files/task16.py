with open('Python/05-Files/Words.txt.') as file:
    count = 0
    line_n=1
    for line in file:
        print(line_n,line,end="")
        count +=1
        line_n +=1
        if count == 5:
            input()
            count = 0
        