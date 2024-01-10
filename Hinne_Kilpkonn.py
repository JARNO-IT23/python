import random
import turtle

#Jarno Orusalu
#28.11.2023
#Hinne: Kilpkonn (IF, FOR)

"""
funktsioon, mis loob erineva suuruse ja asukohaga ringe kogu platsi ulatuses
funktsioon, mis loob erineva suuruse ja asukohaga ruutusid kogu platsi ulatuses
funktsioon, mis kasutab eelmisi funktsioone, et luua suvaliselt ringe ja ristkülikuid
küsib kasutajalt, et mingit atribuuti funktsioonis muuta (näiteks värv, suurus, koguarv)
"""
aken = turtle.Screen()
aken.setup(600,600)
def loo_ring():
    turtle.penup()
    turtle.speed(1000)
    raadius = random.randint(10, 50)
    x = random.randint(-300 , 300)
    y = random.randint(-300 , 300)
    turtle.goto(x, y - raadius)
    turtle.pendown()
    turtle.circle(raadius)

def loo_ruut():
    turtle.penup()
    turtle.speed(1000)
    pikkus = random.randint(20, 100)
    x = random.randint(-200 , 200 )
    y = random.randint(-200 , 200 )
    turtle.goto(x , y )
    turtle.pendown()
    for _ in range(4):
        turtle.forward(pikkus)
        turtle.left(90)


def loo_suvaline():
    turtle.penup()
    valik = random.randint(1,2)
    if valik == 1 :
        loo_ring()
    else :
        loo_ruut()



for _ in range(30):
    loo_suvaline()
    #loo_ring()
    #loo_ruut()


turtle.exitonclick()





