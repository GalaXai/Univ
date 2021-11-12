from mes import Message
class Mail(Message):
    def __init__(self,Sedner,Recipient):
        self.From = Sedner
        self.To = Recipient

    def send(self):
        print("""Sending Email...\nFrom: {}\nTo: {}\nSubject: {}\n{}""".format(self.From,self.To,self.Subject,self.message))
