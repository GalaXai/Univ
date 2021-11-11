class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'
        self.full_name = "Crackow University of Economics"    
    
    def set_name(self, name):
        self.name = name

    def set_fullname(self, name):
        self.full_name = name

    def print_fullname(self):
        print(self.full_name)
    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)

if __name__ == '__main__':
    p0 = University()
    p0.print_name()
    p0.print_fullname()
    
    p1 = University()
    p1.set_name("MIT")
    p1.print_name()
    p1.set_fullname("Massachusetts Institute of Technology")
    p1.print_fullname()