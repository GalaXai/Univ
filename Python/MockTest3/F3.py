#F3.py Zdefiniuj klasę C z atrybutem zawierającym imiona osób zapisanymi w tablicy. 
#Wartość początkowa atrybutu przekazywana jest poprzez parametr konstruktora.
#Dodaj w klasie metodę m(), która zwraca prawdę, gdy imiona się powtarzają lub fałsz w przeciwnym wypadku.

class C():
    def __init__(self,input):
        self.input = input

    def m(self):
        
        x=1
        for word in self.input:
            for i in range(len(self.input) -x):
                if word.lower() == self.input[i+x].lower():
                    return True
            x+=1
        return False
        











print(C(["Anna"]).m())
print(C(["Anna","John"]).m())
print(C(["Anna","John","Anna"]).m())
print(C(["ANNA","John","Anna"]).m())
