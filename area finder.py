q=eval(input("area of circle press 1 , area of rectangle press 2"))
def cir (x):
    a=(3.14)*(x**2)
    print("the area of the circle is",a)
def rec (x,y):
    b=x*y
    print("the area of the rectangle is",b)
if(q==1):
    cir(eval(input("radius")))
elif(q==2):
    rec(eval(input("length")),eval(input("width")))
else:
    print("wrong command")
