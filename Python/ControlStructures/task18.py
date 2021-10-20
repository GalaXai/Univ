pln = int(input())
#pln = pln -(x*5)
reszta = (pln % 5)
x = (pln // 5)

n_reszta = (reszta % 2)
y = reszta // 2
z = (n_reszta // 1)

print(x, y, z)
print("5 zł – " + str(x))
print("2 zł – " + str(y))
print("1 zł – " + str(z))
