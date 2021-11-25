with open('05-Files/numbersPower.txt.','w') as file:
    for i in range(1,10):
        file.write(str(i**1)+','+str(i**2)+','+str(i**3)+'\n')