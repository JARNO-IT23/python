from math import *
#Jarno Orusalu
# 14.11.2023
# Ülesanne 02
"""
Arvusüsteemid
    Kasutaja sisestab täisarvu kümnendsüsteemis
    Sinu programm teisendab selle 2nd ja 16nd süsteemi
"""



"""
Kütusekulu arvutamine
    Kasutaja sisestab tangitud kütuse liitrid
    Kasutaja sisestab läbitud kilomeetrid
    Programm leiab kütusekulu 100km kohta keskmiselt
"""


"""
Ajateisendus
    Kasutaja sisestab aja minutites
    Sinu valem leiab ja väljastab tunnid ja minutid
    Näiteks: sisestus 72, vastus 1:12
"""
aeg = int(input("Sisesta aeg minutites:"))
teisanda = aeg / 60 
print("Aega kulus :",int(teisanda))
"""
Leia kolmnurga hüpotenuus
    Kolmnurga külgede pikkused on a=16 ja b=9
    Kasuta Pythagorase teoreemi (a2 + b2 = c2) ja leia kolmnurga hüpotenuus
"""
a = 16
b = 9 
c =  sqrt(a) + sqrt(b) 
print("Kolmnurga hüpotenuus on ",int(+c))
"""
Rulluisutajad
    Rulluisutaja keskmine kiirus on 29,9km/h
    Kui kaugele jõuab 24minutiga
"""
kiirus = 29.9
aeg = 24
tee_pikkus = kiirus / 60 * aeg
print("Kaugus "+str(round(tee_pikkus,2))+"km")
"""
Pitsa
    Võtsite 3 sõbraga suure pitsa hinnaga 12,90€
    Jätate teenindajale 10% jootraha
    Koosta programm, mis leiab kui palju peab igaüks maksma

"""
sobrad = 3
hind = 12.9
tip = 0.1
kokku = (hind * tip + hind)/sobrad
print("Igaüks maksab "+str(kokku)+"€")

"""
Toote hind
    Toote hind 36,75€
    Soodushind hetkel 40%
    Soovin kolme toote summat
"""
#hind = 36.75
#soodushind = 




"""
Arvutame kolmnurga ümbermõõdu
Loo kolm täisarvulist muutujat a, b, c
Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
"""
a = 5
b = 10
c = 15
p=a+b+c
print("Kolmnurga ümbermõõt on:",p)