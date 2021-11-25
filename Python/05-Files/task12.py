file = open('05-Files/shopping.txt.','a')
file.write(input("What you have to buy: "))
cont = input("Do you want to add a new product ?\ny/n \n")
while cont == 'y':
    file.write(input("What you have to buy: "))
    cont = input("Do you want to add a new product ?\ny/n \n")
file.close