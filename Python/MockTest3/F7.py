#Zdefiniuj klasę C, która umożliwia przetwarzanie dokumentu mockdata.json. Dodaj metodę m(n1,n2),
#która zwraca liczbę rodzin spełniających kryteria: 
#wiek żony co najmniej n1 lat oraz liczba dzieci co najmniej n2. 
#Dodaj metodę m2(n1), która utworzy plik mockdata1.json, zawierający wykaz rodzin, które posiadają co najmniej n1 dzieci.

class C():
    def __init__(self):
        import json
        with open("mockdata.json") as file:
            data = json.load(file)
        self.data = data


    def m(self,n1,n2):
        output = 0
        for test in self.data:
            if (test["wife"])["age"] > n1  and (test["wife"])["age"] < n2:
                output+=1
        return output
                
    def m2(self,n1):
        output = 0
        for test in self.data:
            if len(test["children"]) >= n1:
                output +=1
        return output


print(C().m(30,40))
print(C().m2(1))