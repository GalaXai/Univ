with open("PY4E/Files/mbox-short.txt","r") as file:
    lista = file.readlines()
    for li in lista:
        print(li.upper())