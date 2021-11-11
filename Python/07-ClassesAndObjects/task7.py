class University():
    # object constructor (__init__ method)
    def __init__(self):
        # object states/attributes (fields)
        self.name = 'CUE'    
        # object bahaviors (methods)
    def print_name(self):  
        print(self.name)
if __name__ == '__main__':
    s1=University()
    s1.print_name()

