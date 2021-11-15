with open('Python/05-Files/shoppionglist.txt.','w') as file:
    f = open('Python/05-Files/MeatAndFish.txt.','r')
    m = open('Python/05-Files/GrainsAndBread.txt.','r')
    for line in f:
        file.write(line) 
    for line in m:
        file.write(line)
    f.close()
    m.close()