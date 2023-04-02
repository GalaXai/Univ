class C():
    def __init__(self):
        import xml.etree.ElementTree as et
        tree = et.parse('data.xml')
        self.root = tree.getroot()

    def m(self):
        i=0
        for data in self.root[0]:
            print(data.text)
            i+=1

C().m()