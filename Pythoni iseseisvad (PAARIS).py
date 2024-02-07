#Jarno Orusalu 
#16.01
import random 
import math


"""
2. Vanused
loo vanuste loend 1p
leia numbrite suurim ja vÃ¤ikseim arv 1p
kogusumma 1p
keskmine 1p
"""	
vanused = [5,16,32,98,41,25, 30, 22, 40, 18, 28, 35, 27, 33, 70] 
suurim = max(vanused)
vahim = min(vanused)
kogusumma = sum(vanused) 
keskmine = kogusumma / len(vanused)
   
print(f"Vanused: {vanused}")
print(f"Väikseim vanus: {vahim}")
print(f"Keskmine: {keskmine}")
print(f"Suurim vanus: {suurim}")

"""
4. List Less Than Ten
Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
Write this in one line of Python. 1p
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 1p
"""	

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("Elements less than 5:")
for element in a:
    if element < 5:
        print(element)

print("One-liner:", [element for element in a if element < 5])


number = float(input("Enter a number: "))

filtered = [element for element in a if element < number]
print(f"Elements less than { number }: {filtered}")

"""
6. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vÃµi paaritu
kuvatakse korrektne arusaadav kÃ¼simus ja vastus - 1p
eelnev kontroll, kas kasutaja ei lisanud arvu vÃµi pani nulli - 1p
kood mis teavitab paaris vÃµi paaritust arvust - 1p
kuvatakse programmi pealkiri - 1p
kood kommenteeritud - 1p
"""
print("......................Paaris-Paaritu Kontrollija.........................")
sisestus = input("Sisesta arv (või vajuta Enter, et lõpetada): ")
if sisestus:
    try:
        arv = int(sisestus)

        if arv % 2 == 0:
            print(f"{arv} on paaris arv.")
        else:
            print(f"{arv} on paaritu arv.")
    except ValueError:
        print("Sisestatud väärtus ei ole arv. Palun sisesta täisarv.")
else:
    print("Sisestati tühi väärtus või vajutati Enter. Programm lõpetatakse.")

"""
8. TÃ¤ringud
kuvatakse korrektne arusaadav kÃ¼simus ja hiljem vastus - 1p
kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu - 1p
kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale - 2p
kood kommenteeritud - 1p
"""	
def veereta():
    return random.randint(1, 6), random.randint(1, 6)

print(".................Täringute Mäng..................")

arvuti = 100
kasutaja = 100

while True:
    
    pakkumine = int(input(f"Sinu hetke rahakott: {kasutaja}. Tee pakkumine (1-6 punkti): "))
    if 1 <= pakkumine <= 6:
        taringud = veereta()
        arvuti = sum(taringud)
        kasutaja = pakkumine + random.randint(1, 6)
        print(f"Arvuti tulemus: {arvuti}")
        print(f"Sinu tulemus: {kasutaja}")
        if kasutaja > arvuti:
            kasutaja += 10
            arvuti -= 10
            print("Sa võitsid!")
        elif kasutaja < arvuti:
            kasutaja -= 10
            arvuti += 10
            print("Arvuti võitis!")
        else:
            print("Viik!")
    else:
        print("Vigane sisend. Sisesta number 1-6.")
        continue








