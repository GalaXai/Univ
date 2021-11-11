import random
class m_thermo:
    def __init__(self):
        self.temperature = random.randrange(360,420)

    def display(self):
        if self.temperature >= 410:
            print("Temperature: {}C ".format(self.temperature/10) + "CRITICAL TEMPERATURE!!")
        elif self.temperature >= 370:
            print("Temperature: {}C (fever)".format(self.temperature/10))
        
        else:
            print("Temperature: {}C".format(self.temperature/10))

if __name__ == '__main__':
    for x in range(10):
        p = m_thermo()
        p.display()
