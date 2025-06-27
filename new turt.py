import time
import turtle
x=turtle.Turtle()
y=turtle.Screen()
x.turtlesize(0.8)
x.shape('turtle')
x.turtlesize(1.5)
x.color("orange")
def zz ():
    x.write("INSTRUCTIONS: \n up key forward\ndown key backward\n right key right\n left key left\n 2key lift pen up\n 1 key pen down",font=("Ariel",26,"normal"))
y.screensize(200,200)
H=zz()
print(H)
time.sleep(5)
x.undo()
x.write("PROGRAMME STARTS IN ",align="center",font=("Ariel",26,"bold"))
time .sleep(2)
x.undo()
x.write("3 ",align="center",font=("Ariel",26,"bold"))
time .sleep(1)
x.undo()
x.write("2 ",align="center",font=("Ariel",26,"bold"))
time .sleep(1)
x.undo()
x.write("1 ",align="center",font=("Ariel",26,"bold"))
time .sleep(1)
x.undo()
x.right(-90)
def fun1 ():
    x.fd(10)
def fun2 ():
    x.back(10)
def fun3 ():
    x.right(90)
def fun4 ():
    x.left(90)
def fun5 ():
    x.penup()
def fun6 ():
    x.pendown()
y.listen()
y.onkey(fun1,"Up")
y.listen()
y.onkey(fun2,'Down')
y.listen()
y.onkey(fun3,'Right')
y.listen()
y.onkey(fun4,"Left")
y.listen()
y.onkey(fun5,"2")
y.listen()
y.onkey(fun6,"1")


