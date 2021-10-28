file = open('python/05-Files/countries.txt.','w')
Countries = ["Poland" , "Germany" , "Sweden" , "Canada" , "Japan"]
for x in Countries:
    file.write(x+"\n")
file.close

file = open('python/05-Files/countries.txt','r')
file_content = file.read()
print( file_content )
file.close()
