from mes import Message
class SMS(Message):
    def __init__(self,Sender,Recipient):
        self.From = str(Sender)
        self.To = str(Recipient)

    def send(self):
        print("""Sending SMS...\nFrom: {}\nTo: {}\nSubject: {}\n{}""".format(self.From,self.To,self.Subject,self.message))
