from mail import Mail
from sms import SMS

class sendEmail(Mail):
   def __init__(self, Sender, Recipient):
       super().__init__(Sender, Recipient)

   def send(self):
       return Mail.send(self)

class sendSMS(SMS):
    def __init__(self, Sender, Recipient):
        super().__init__(Sender, Recipient)

    def send(self):
        return SMS.send(self)

if __name__ == '__main__':
    x=sendSMS(11122333,999888777)
    x.write("meeting on Thursday","i would like to inform you that our Thursday meeting has been canceled")
    x.send()
    print()
    y=sendEmail("teanj@gmial.com","Qanmi@outlook.com")
    y.write("meeting on Thursday","i would like to inform you that our Thursday meeting has been canceled")
    y.send()