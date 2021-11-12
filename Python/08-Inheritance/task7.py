class Message():
    def __init__(self):
        self.message = ''
    
    def set_message(self,message):
        x = message
        x = x.capitalize()
        self.message = x + " BYE"

    def __str__(self):
        return self.message

if __name__ == '__main__':
    m = Message()
    m.set_message("hello")
    print(m)
