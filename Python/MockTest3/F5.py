#Zdefiniuj klasę C z atrybutem tekstowym t. Wartością atrybutu t jest dowolny tekst  przekazany poprzez parametr konstruktora. 
#Metoda m1() zwraca słownik zawierający liczbę wystąpień poszczególnych znaków w tekście t. 
#Metoda m2(c1) zwraca słownik zawierający liczbę wystąpień znaków wymienionych w c1.


class C():
    def __init__(self,input):
        self.input = input
        pass

    def m1(self):
        import re
        output = {

        }
        letters = re.findall(".",self.input)
        for letter in self.input:
            output[letter] = letters.count(letter)
        return output

    def m2(self,data):
        import re
        output = {

        }
        letters = re.findall(".",self.input)
        let = re.findall(".",data)
        for x in let:
            output[x] = letters.count(x)
        return output
        




print(C("my moon").m1())
print(C("my moon").m2("mn"))
