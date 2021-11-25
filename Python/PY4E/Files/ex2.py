import re
with open("PY4E/Files/mbox-short.txt","r") as file:
    count = 0
    amm = 0
    lista = file.read()
    x = re.findall("X-DSPAM-Confidence: \d\.\d{4}",lista)
    for string in x:
        y = re.findall("\d.\d{4}",string)
        count +=1
        amm += float(y[0])
    print(file.name)
    print( amm/count )
print('\n')
with open("PY4E/Files/mbox.txt","r") as file:
    count = 0
    amm = 0
    lista = file.read()
    x = re.findall("X-DSPAM-Confidence: \d\.\d{4}",lista)
    for string in x:
        y = re.findall("\d.\d{4}",string)
        count +=1
        amm += float(y[0])
    print(file.name)
    print( amm/count )