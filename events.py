import turtle as t
x=t.Screen()
y=t.Turtle()

def d():
    y.fd(100)
x.listen()
x.onkey(d,"Up")
