class stats:
    def __init__(self,*args):
        self.number = []
        for arg in args:
            self.number.append(arg)


    def addNumbers(self,*args):
        for arg in args:
            self.number.append(arg)
        return(self.number)

    # def display(self):
    #     for num in self.number:
    #         print(num, end=" ")

    def mean(self):
        return(sum(self.number)/len(self.number))

    def median(self):
        self.number.sort()
        x=len(self.number)
        if x % 2 == 0:
            return((self.number[int(x/2)-1] + self.number[int((x/2))])/2)
        else:
            return(self.number[int(x/2)])

    def gratest(self):
        z = self.number[0]
        for x in range(len(self.number)):
            if z < self.number[x]:
                z = self.number[x]          
        return z

    def smallest(self):
        z = self.number[0]
        for x in range(len(self.number)):
            if z > self.number[x]:
                z = self.number[x]   
        return z    

    def display(self):
        print("{}\nGreatest number = {}\nSmallest number = {}\nArithmetic mean of numbers = {}\nMedian = {}".format(
            self.number,self.gratest(),self.smallest(),self.mean(),self.median()))

if __name__ == '__main__':
    p0 = stats(12, 37, 6, 9, 17)
    p0.display()




