file = open('python/05-Files/countries.txt','r')
for line in file:
    print(line,end="")
file.close()
