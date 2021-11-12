class Message():
    def __init__(self):
        self.message = ''
    
    def write(self,Subject,message):
        x = message
        x = x.capitalize()
        self.Subject = Subject.capitalize()
        self.message = x + " bye"

    def __str__(self):
        return self.message
