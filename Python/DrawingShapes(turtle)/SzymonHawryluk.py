
import turtle


class draw():
    import turtle
    WIDTH, HEIGHT = 360, 360

    screen = turtle.Screen()
    screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    turtle.speed(10)
    turtle.tracer(0)
    
    def setup(self,x,y,color = "black",width = 1):
        printer = turtle.pen()
        turtle.pen(printer,pencolor=color ,pensize= width)
        turtle.up()
        turtle.setposition(x,y)
        turtle.down()

    def draw_circle(self,x=0,y=0,size=1,color = "black",width = 1):
        
        self.setup(x,y,color,width)

        for i in range(360):
            turtle.forward(size*1)
            turtle.right(1)

    def draw_ring(self,x=0,y=0,size=1,color = "black" , width = 1):
        self.setup(x,y,color,width)
        for i in range(360):
            turtle.forward(size *1)
            turtle.right(1)
        turtle.right(90)
        turtle.up()
        turtle.forward(size*30)
        turtle.down()
        turtle.left(90)
        for i in range(180):
            turtle.forward(size*1)
            turtle.right(2)

    def draw_cross(self,x=0,y=0,size=1,color = "black" , width = 1):

        self.setup(x,y,color,width)

        turtle.forward(size*40)
        turtle.right(90)
        turtle.forward(size*40)
        for i in range(3):
            turtle.left(90)
            turtle.forward(size*40)
            turtle.right(90)
            turtle.forward(size*40)
            turtle.right(90)
            turtle.forward(size*40)
        turtle.left(90)
        turtle.forward(size*40)

    def draw_quatrefoil(self,x=0,y=0,size=1,color = "black" , width = 1):
        
        self.setup(x,y,color,width)
        
        for i in range(4):
            turtle.left(90)
            for i in range(180):
                turtle.forward(size*0.5)
                turtle.right(1)
    
    def draw_polygon(self,x=0,y=0,size=1,color = "black" , width = 1):
        import random
        self.setup(x,y,color,width)
        start = turtle.position()
        for i in range(random.randrange(3,8)):
            turtle.right(random.randrange(10,90))
            turtle.forward(size*50)
        turtle.goto(start)
        
    def draw_me(self):
        turtle.up()
        turtle.goto(700,700)
        turtle.down()
        turtle.write("Szymon Hawryluk ZZISS1-1111",font=("Arial", 16, 'normal', 'bold', 'italic'))
    


if __name__ == '__main__':
    test = draw()
    test.draw_circle(100,600)
    test.draw_circle(100,350,2,"yellow",4)
    test.draw_circle(0,0,2,"pink",2)
    test.draw_circle(0,0,1,"red",3)
    test.draw_circle(0,0,3,"yellow",4)

    test.draw_ring(200,200)
    test.draw_ring(300,300,1,"red",3)
    test.draw_ring(-200,400,2,"black",2)
    test.draw_ring(-400,300,3,"blue",1)
    test.draw_ring(300,450,1,"green",2)
    
    test.draw_cross(0,400)
    test.draw_cross(150,-100,1,"blue",2)
    test.draw_cross(-400,400,2,"red",3)
    test.draw_cross(600,400,2,"red",3)
    test.draw_cross(600,-600,1,"black",3)
   
    test.draw_quatrefoil(-200,-100,1,"green",4)
    test.draw_quatrefoil(-600,600,1,"pink",3)
    test.draw_quatrefoil(-600,400,2,"blue",2)
    test.draw_quatrefoil(-600,0,2,"red",4)
    test.draw_quatrefoil(600,0,2,"yellow",4)
    
    test.draw_polygon(300,100,1,"red",2)
    test.draw_polygon(400,270,2,"black",3)
    test.draw_polygon(0,100,1,"blue",1)
    test.draw_polygon(0,200,1,"pink",2)
    test.draw_polygon(0,300,2,"brown",2)
    
    test.draw_me()
    test.setup(-10000,10000)
    test.turtle.forward(1)
    input()