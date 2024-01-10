#Jarno Orusalu
# kilpkonna ülesanded 01-02

import turtle

edasi = 100

#akna seaded
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Ülesanded 1 J.Orusalu")

#kilpkonnad
l = turtle.Turtle()
l.color("blue")
l.forward(edasi)

r = turtle.Turtle()
r.color("red")
r.left(45)
r.fd(edasi)

d = turtle.Turtle()
d.color("purple")
d.left(90)
d.fd(edasi)

mm = turtle.Turtle()
mm.color("orange")
mm.left(135)
mm.fd(edasi)

l = turtle.Turtle()
l.color("blue")
l.left(180)
l.forward(edasi)

r = turtle.Turtle()
r.color("red")
r.left(-45)
r.fd(edasi)

d = turtle.Turtle()
d.color("purple")
d.left(-90)
d.fd(edasi)

mm = turtle.Turtle()
mm.color("orange")
mm.left(-135)
mm.fd(edasi)

turtle.exitonclick()
