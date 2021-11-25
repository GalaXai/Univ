file = open('05-Files/numbers.txt.','w')
for x in [5,3,1,7,21,4,5,2]:
    file.write(str(x)+"\n")
file.close

file = open('05-Files/numbers.txt.','r')
wynik = 0
for num in file:
    wynik += int(num)
print(wynik)