colors = ["olive","yellow","navy","navy","silver","red","blue"]
#text file work?
file = open("04-Arrays/task15.txt","w")
for i in range(len(colors)):
    file.write(colors[i]+"\n")
file.close()