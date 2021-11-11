class bankAccount:
    def __init__(self,accountNumber):
        self.accountNumber = accountNumber
        self.balance = 0

    # number XX,XX
    def deposit(self,number):
        x=2
        z=0
        while number % 1 > 0 or z < 2:
            number *=10
            z+=1 
        y=int(number)*10**(x-z)
        self.balance += y
    
    def withdraw(self,number):
        x=2
        z=0
        while number % 1 > 0 or z < 2:
            number *=10
            z+=1 
        y=int(number)*10**(x-z)
        if self.balance - number < 0:
            print("Insufficient funds on the account")
            return 0
        self.balance -=number

    def display(self):
        print("Bank Account No: {}\nBalance: PLN {}".format(self.accountNumber,(int(self.balance)/100)))

if __name__ == '__main__':
    p0 = bankAccount("12 3456 5555 9090 1111 0000 7722")
    p0.display()
    p0.deposit(25.30)
    p0.display()
    p0.withdraw(31.70)
    p0.display()
    p0.withdraw(14)
    p0.display()
