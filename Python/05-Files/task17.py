with open('05-Files/Copy.txt.','w') as file:
    f = open('05-Files/Words.txt.','r')
    for line in f:
        file.write(line)
    f.close