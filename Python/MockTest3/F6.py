#Zdefiniuj klasę C, która zawiera tablicę wartości logicznych. Tablica przekazana jest poprzez parametr konstruktora. 
#Metoda m() zwraca liczbę elementów tablicy, dla których obydwa sąsiadujące elementy mają wartość przeciwną.

class C():
    def __init__(self,input):
        self.input = input

    def m(self):
        value = 0
        for i in range(1,len(self.input)-1):
            if self.input[i-1] != self.input[i] and self.input[i] != self.input[i+1]:
                value +=1
        return value    

print(C([True,False,False]).m())
print(C([True,False,True,False]).m())
print(C([True,False,True,True,False,True,False,True,False]).m())
