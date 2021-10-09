class Redbull:
    def __init__(self, flavor, color, score):
        self.flavor = flavor
        self.color = color
        self.score = score

    def addRedbull(self):
        listR.append(self)

    def printList():
        for x in listR:
            print("Redbull o smaku {}, ma kolor puszki {}, moja ocenta to {}".format(
                x.flavor, x.color, x.score))

    def averageScore():
        sum = 0
        for x in listR:
            sum += x.score
        wynik = sum/listR.__len__()
        print(wynik)


listR = []
watermelon = Redbull("watermelon", "red", 20)
winteredition = Redbull("iceberry", "light blue", 5)
blueberry = Redbull("blueberry", "blue", 1)


Redbull.addRedbull(winteredition)
Redbull.addRedbull(watermelon)
Redbull.addRedbull(blueberry)
Redbull.printList()
Redbull.averageScore()
