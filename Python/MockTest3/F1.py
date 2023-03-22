#(F1.py) Zdefiniuj klasę C, która zawiera atrybuty name oraz surname. 
#Wartości początkowe atrybutów przekazywane są poprzez parametry konstruktora.  
#Określ tekstową reprezentację obiektu, składającą się z pierwszych liter imienia oraz nazwiska. 
#Inicjały pisane wielkimi literami. Przykład:
#C("anna","may") => "AM"

class C():
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name[0].upper()}{self.surname[0].upper()}'



print(C("anna","may"))