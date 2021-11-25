import re
def f3(t):
    output = 0
    #t == stirng:
    x = re.findall("\d{2,}",t)
    for i in x:
        if len(i) > 3:
            x.remove(i)
    for z in x:
        output +=int(z)
    return output

print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"))
