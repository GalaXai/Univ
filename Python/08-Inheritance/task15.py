class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, other):
        x=0
        y=0
        if self.x == other.x:
            if self.y == other.y:
                print ("The distance between them is 0")
        else:
            x= self.x - other.x
            y= self.y- other.y
            print("The distance between them is {:.2f}".format((x**2+y**2)**(1/2)))
            print (f'The distance between them is {(x**2+y**2)**(1/2)}')
            print(f"Vector is euqal to ({x},{y})")
            #print ("The distance between them is {:.2f}".format((x**2+y**2)**(1/2))


if __name__ == '__main__':
    p0 = Point(3,4)
    p1 = Point(1,1)
    (p0 == p1)
    p2 = (1,1)
    