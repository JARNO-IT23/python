#Jarno Orusalu
# kilpkonna KT number 4

import turtle 

edasi=100
Korda=5

def joonistanelinurga(pikkus,arv):
    k = turtle.Turtle()
    for j in range(arv):
        k.lt(360/arv)
        k.fd(pikkus/2)
        k.lt(90)
        for i in range(3):
            k.fd(pikkus)
            k.lt(90)
        k.fd(pikkus/2)
        
        
joonistanelinurga(edasi,Korda)