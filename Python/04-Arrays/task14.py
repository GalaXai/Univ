names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
def longestWord(names):
    x=0
    for lenght in names:
        y=(len(lenght))
        if y>x:
            x=y
            name = lenght
    return name
#names.sort() #Alphabetic Sort
print(names)
print(longestWord(names))