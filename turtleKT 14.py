

import turtle 

edasi=100
Korda=5

def neliteist(pikkus,arv):
  nurk=360/5
  k = turtle.Turtle()
  for i in range (20):
     k.right(nurk)
     k.color("white")
     k.forward(-100)
     k.color("black")
     k.right(90)
     k.forward(100)
     k.left(90)
     k.backward(-100)
     k.left(90)
     k.color("white")
     k.forward(100)
    
        
        
neliteist(edasi,Korda)