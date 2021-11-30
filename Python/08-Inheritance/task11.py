class Student():
    id_count = 100001
    def __init__(self,name,surname,fieldOfStudy):
        self.name = name
        self.surname= surname
        self.fieldOfStudy = fieldOfStudy
        self.id = Student.id_count
        self.Univ = "AGH"
        Student.id_count +=1
    
    def __str__(self):
        return f'{self.name} {self.surname} {self.id}, {self.fieldOfStudy},{self.Univ}'

if __name__ == '__main__':
    p0 = Student("Szymon","Hawryluk","ApliedInformatics")
    print(p0)
    p1 = Student("Szymon","Hawryluk","ApliedInformatics")
    print(p1)