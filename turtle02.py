#Jarno Orusalu
# kilpkonna ülesanded 01-02

import turtle

#akna seaded
aken = turtle.Screen()
aken.setup(600,600)
aken.title("Ülesanded 2 J.Orusalu")

edasi = 100
nurk = 144
kokku =5
varv = "red"
def joonistaKolmnurk(l,c):
    #print(l, c)
    don = turtle.Turtle()
    don.color(c)
    for x in range(3):
        don.fd(-l)
        don.right(120)
        
        
        
#kilpkonnad
leo = turtle.Turtle()
for x in range (kokku):
    leo.forward(edasi)
    leo.right(nurk)
    
joonistaKolmnurk(edasi, varv)


turtle.exitonclick()
