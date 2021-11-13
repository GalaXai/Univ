class Calc():

    @staticmethod
    def s_Circle(r):
        print(f"Surface area of circle is euqal to : {r*3.14}")

    @staticmethod
    def s_Triangle(base,height):
        print(f"Surface area of triangle is euqal to : {base *height /2}")

    @staticmethod
    def s_Rectangle(side1,side2):
        print(f"Surface area of rectangle is euqal to : {side1*side2}")

if __name__ == '__main__':
    Calc.s_Circle(3)
    Calc.s_Rectangle(4,7)
    Calc.s_Triangle(6,2)