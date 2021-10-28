def LinesInFile(filename):
    with open('python/05-Files/{}.txt.'.format(filename)) as file:
        Line = 0
        for lines in file:
            Line +=1
        print("File name: {}.txt".format(filename))
        print("Number of lines: {}".format(Line))

LinesInFile("countries") #flename