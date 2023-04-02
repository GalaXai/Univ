#Zdefiniuj klasę C, która umożliwia przetwarzanie dokumentu mockdata.xml.
#Dodaj metodę m(n1,n2), która zwraca liczbę rodzin spełniających kryteria:
#wiek żony co najmniej n1 lat oraz liczba dzieci co najmniej n2.
class C():

    def __init__(self):
        import xml.etree.ElementTree as et
        tree = et.parse('mockdata.xml')
        self.root = tree.getroot()
    def m(self,n1,n2):
        i=0
        output =0
        for i in range(10):
            v1 =[]
            v2 =[]
            for a in self.root[i][2]:
                v1.append(a.text)
            
            for b in self.root[i][3]:
                v2.append(b.text) 

            if int(v1[1]) > n1 and len(v2) > n2:
                output +=1
            i+=1
        return output
        

print(C().m(30,2))
