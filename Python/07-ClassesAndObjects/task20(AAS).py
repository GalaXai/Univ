class Contact:
    def __init__(self,name,email,telephone):
        self.name = name
        self.email = email
        self.telphone = telephone
        self.addContact()

   
    def addContact(self):
        listC.append(self)

    def display():
        for x in listC:
            print("Name: {}  Email: {}  Telephone: {}".format(
                x.name,x.email,x.telphone))


listC=[]
p1=Contact("John Brown","brown@onet.pl",555234000)
p2=Contact("Anna May","am@o2.pl", 232000199)
p3=Contact("George Small","smallg@google.pl",222999100)
p4=Contact("Paola Big ","bigpaola@poczta.pl",100200300)
if __name__ == '__main__':
    Contact.display()