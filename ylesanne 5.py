#J.Orusalu
#28.11.2023
"""
Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm.
"""
vanused = [69, 1, 22, 99, 28, 18, 90, 48]

for vanus in vanused:
    print('*' * vanus)


"""
Vanused
     Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine
"""
vanused = [25, 80, 57, 44, 69, 18, 49, 12]

suurim_vanus = max(vanused)
vahim_vanus = min(vanused)
kogusumma = sum(vanused)
keskmine = kogusumma / len(vanused)

print("Suurim vanus:", suurim_vanus)
print("Väikseim vanus:", vahim_vanus)
print("Kogusumma:", kogusumma)
print("Keskmine vanus:", keskmine)




"""
Duplikaadid
    Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
    opilased = ['Juhan'','Kati','Mario','Mario','Mati','Mati']
    Loo kood, mis ei väljasta kordusi.
"""
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
nimed=[]

for opilane in opilased:
    if opilane not in nimed:
        nimed.append(opilane)

print(nimed)

"""
Õpilased
    Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
    opilased = ['Juhan','Kati','Maarja','Mario','Mati']
"""
nr = 1
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
for opilane in opilased:
    print(f"{nr}.{opilane}")
    nr+=1

valik = int(input("Mitmedat nime soovid muuta: "))
del opilased[valik-1]
uus_nimi = input("Lisa uus või paranda nimi: ")
opilased.insert(valik-1, uus_nimi)



nrs = 1
for opilane in opilased:
    print(f"{nrs}.{opilane}")
    nrs+=1



"""
Nimede lisamine loendisse
    Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.
"""
nimed = []

for i in range(5):
    nimed = input("Lisa nimi: ")
    nimed.append:(nimed)


print(nimed) 








