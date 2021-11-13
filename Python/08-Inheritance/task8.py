import random
class Cell_Phone():
    def __init__(self,name,os,producer):
        self.name = name
        self.os = os
        self.producer = producer
        self.battery = random.randrange(0,100)



    
    
    def __str__(self):
        return "{} has installed {} OS, made by {} has {}% battery".format(self.name,self.os,self.producer,self.battery)

if __name__ == '__main__':
    p0 = Cell_Phone("GalaxyS10","Android12","Samsung")
    print(p0)