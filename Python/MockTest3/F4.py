#Zdefiniuj klasę C, która zawiera słownik z wartością zapisaną w systemie pozycyjnym (od dwójkowego do dziesiętnego).
#Słownik przekazywany jest poprzez parametr konstruktora.
#Metoda m() zwraca wartość w systemie dziesiętnym lub -1, gdy podana w słowniku wartość jest niegodna z podanym systemem liczbowym


class C():
    def __init__(self,input):
        self.input = input
        pass

    def m(self):
        val = 0
        x = int(self.input["system"])
        i = len(self.input["value"]) -1
        for num in self.input["value"]:
            val += int(num) * x**i
            if int(num) >= x :
                return -1
            i-=1
        return val





print(C({"system":"2", "value":"101"}).m())
print(C({"system":"8", "value":"70281"}).m())
print(C({"system":"10", "value":"70291"}).m())
