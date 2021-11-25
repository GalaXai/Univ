import random
with open('05-Files/random.txt.','w') as file:
    for i in range(50):
        file.write(str(random.randrange(100,990))+"\n")