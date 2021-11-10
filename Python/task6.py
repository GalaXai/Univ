import random
class book:
    def __init__(self,page,chapter,line):
        self.page = page
        self.chapter = chapter
        self.line = line
    
    def add_State(self):
        listR.append(self)
    
    def stateOfBook():
        for x in listR:
            print("Page {}, chapter {}, line {}".format(x.page,x.chapter,x.line))
listR = []
test1 = book(random.randint(6,200), random.randint(0,6), random.randint(0,50))
book.add_State(test1)
#=======================#
class Telephone_connection:
    def __init__(self,isconnected,speakerON,muted):
        self.isconnected = isconnected
        self.speakerON = speakerON
        self.muted = muted
    
    def add_State(self):
        listP.append(self)
    
    def stateOfConecction():
        for p in listP:
            print("Is it connected? {}, is the speaker on? {}, is the microphone muted? {}".format(p.isconnected,p.speakerON,p.muted))
listP = []
choose=[False,True]
test2 = Telephone_connection(random.choice(choose), random.choice(choose), random.choice(choose))
Telephone_connection.add_State(test2)
#=======================#
class Studnets:
    def __init__(self,name,surname,Grade):
        self.name = name
        self.surname = surname
        self.Grade = Grade
    
    def add_State(self):
        listS.append(self)

    def stateOfStudents():
        for s in listS:
            print("Name {}, Surname {}, his grade is = {}".format(s.name,s.surname,s.Grade))

listS=[]
grades=[2,2.5,3,3.5,4,4.5,5,5,5]
test3 =Studnets("Szymon","Hawryluk",random.choice(grades))
Studnets.add_State(test3)
if __name__ == '__main__':
    book.stateOfBook()   
    Telephone_connection.stateOfConecction()
    Studnets.stateOfStudents()