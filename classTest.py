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
        print("Średnia ocena {:.1f}".format(wynik))


listR = []
watermelon = Redbull("watermelon", "red", 80)
winteredition = Redbull("iceberry", "light blue", 70)
blueberry = Redbull("blueberry", "blue", 70)


Redbull.addRedbull(winteredition)
Redbull.addRedbull(watermelon)
Redbull.addRedbull(blueberry)
Redbull.printList()
Redbull.averageScore()


