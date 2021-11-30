class University():
    
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return self.name + " is the best!"

if __name__ == '__main__':
    my_university = University('AGH')
    print(my_university)
