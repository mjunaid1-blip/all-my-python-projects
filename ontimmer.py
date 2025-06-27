import turtle as t
t.Screen()
def a():
    t.fd(100)
    t.right(90)
    t.ontimer(a(),1000)
a()
