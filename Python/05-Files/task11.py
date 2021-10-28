film_titles = ["Dune","Venom","Antlers","Hallowen Kills","Luca"]
file = open('python/05-Files/films.txt.','w')
for title in film_titles:
    file.write(title+"\n")
file.close