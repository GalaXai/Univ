class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'AGH'    
    
    def set_name(self, name):
        self.name = name

    # object bahaviors (methods)
    def print_name(self):  
        print(self.name)

if __name__ == '__main__':
    p1 = University()
    p1.set_name("MIT")
    p1.print_name()