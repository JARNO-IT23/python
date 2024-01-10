import random 
#Jarno Orusalu
# 21.11.2023
# Ülesanne 03

#print(f"Tere {nimi} {pnimi}!")
"""
Ruutude ja kuupide tabel
    Programm leiab ja väljastama ruudud ja kuubid arvudele 1..10.
    Vorminda tabel tulpades.
"""
for i in range (1,11):
    print(f"{i:2}{i**2:4}{i**3:4}")

"""
Pank
    Kasutaja soovib panka panna raha teatud aastateks.
    Panga intress on 5% summast. Leia kui palju ta summa iga aasta kasvab.
    Vorminda tabel tulpades.
"""
raha = 10000
konto = raha
aastad = 5
intress = 0.05
print(f"Aasta   Algsumma    Intress    Aastalõpuks")
for i in range(aastad):
    print(f"{i+1:<7} {konto:.2f} {konto*0.05:9.2f}{konto + konto * intress:13.2f}")
    konto = konto + konto * intress
print(f"Summa Kokku: {round(konto,2)}")
print(f"Kasum: {round(konto - raha ,2)}") 

"""
Arvamismäng
    Kasutaja saab arvata arvuti poolt loodud arvu 3 korda.
    Õnnitle kasutajat, kui arvas selle ära.
    Kui mitte, siis küsi, kas ta soovib veel arvata.
"""

print ("Arva arv 1-10\n-----------------")
suvArv = random.randint(1,10)

for i in range(3):
    vastus = int(input("Sinu arv "))
    if suvArv == vastus :
        print("Arvasit ära" )
        break
    else:
        print("Proovi uuesti")
print ("Game over")
uusmang = input("Soovit uut mängu?  jah/ei:  ")
if uusmang == "ei":
  u


"""
Viisikud
    Programm väljastab ainult 5ga jaguvad arvud 1-100
"""
for a in range (1,101):
    if  a%5 == 0:
        print (a)
"""
Pisike korrutustabel
    Koosta programm, mis tekitab automaatselt viiega korrutustabeli.
"""
arv = 5

for i in range(1,11):
   print(arv,'x',i,'=',arv*i)
"""
Paaris ja paaritu
    Loo tsükkel, mis genereerib arvud 1-100 koos vastava tekstiga, kas arv on paaris või paaritu
"""
for arv in range (21):
    if arv % 2 == 0:
        v = "paaris"
    else:
        v = "paaritu"

print(arv, v)

"""
Tärnid
    Loo tsükkel, mis väljastab 5×5 tärnid
    Loo tsükkel, mis väljastab tärnidest kasvava kolmnurga
    Loo tsükkel, mis väljastab tärnidest kahaneva kolmnurga
"""
for i in range(1,6):           
    for j in range(1,6):       
        print('* ', end='')
    print()
    
print ( )    
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()
    

"""
Jalgpalli meeskond
    Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
    Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
    Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
"""
sugu = input("Mis on teie sugu? ")
if  sugu == "m" :
    vanus = int(input("Mis on teie vanus? "))
    if vanus >= 16 and  vanus<=18 :
        print ("Pääseb meeskonda!")
    else:
        print ("Vanus ei sobi")
else:
    print("Sugu ei sobi!")


"""
Müük
    Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€,
    saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
    Kuva toote lõplik hind.
"""
hind  = 20


if hind <=  10:
    soodukas = 0.1
else:
    soodukas = 0.2

loplik_hind = hind - hind * soodukas 

print(loplik_hind)


"""
Juubel
    Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
"""
a = 15
if a % 5 == 0:
    v = "on"
else:
    v = "ei ole "
print(f"vanus: {a} {v} juubel")

"""
Matemaatika
    Kasutaja sisestab kaks arvu ning programm küsib kasutajalt,
    mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
"""
arv1 = int(input("Sisesta külg 1: "))
arv2 = int(input("Sisesta külg 2: "))
tehe = input ("Vali tehe (+ - * /): ")

if tehe == "+":
    vastus = arv1 + arv2
elif tehe == "-":
    vastus = arv1 - arv2
elif tehe == "*":
    vastus = arv1 * arv2
elif tehe == "/":
    vastus = arv1 / arv2
else:
    vastus = "Seda valikut pole"
    
print(f"{arv1}{tehe}{arv2} = {vastus}")

"""
Ruut
    Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
"""

arv1 = input ("Sisesta külg 1: ")
arv2 = input ("Sisesta külg 2: ")

if  arv1 == arv2:
    print("Võimalik, et saab ruudu")
else:
    print("Nii ei saa ruudu teha")


