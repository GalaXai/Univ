class C():
    def __init__(self,input):
        self.input = input


    def m(self):
        import re
        letters = re.findall("\w",self.input)
        for let in self.input:
            if letters.count(let) > 1:
                return False
        return True


print(C("red sun").m())
print(C("blue water").m())
print(C("BLUE water").m())
