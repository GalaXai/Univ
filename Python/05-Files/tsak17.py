with open('python/05-Files/Copy.txt.','w') as file:
    f = open('Python/05-Files/Words.txt.','r')
    for line in f:
        file.write(line)
    f.close