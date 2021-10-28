file = open('python/05-Files/UserData.txt.','w')
Name = input("Whats your name: ")
Surname = input("Whats your Surname: ")
Study = input("What are you studing: ")
file.write("Name-{}\nSurname-{}\nField of Study-{}".format(Name,Surname,Study))
file.close