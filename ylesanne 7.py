# J_0rusalu
# 05.12.2023

def tervita(nimi, keel="ge"):
    if keel =="en":
        print(f"Hi {nimi}")
    elif keel == "et":
        print(f"Tere {nimi}")
    else:
        print(f"hallo {nimi}")

tervita("jarno","en")
tervita("jarno")


print(****************** Mega Hea Kalkulaator ************************************)

import math

while True:
    print("Valige kujund:")
    print("1. Kuup")
    print("2. kera")
    print("3. koonus")
    print("4. silinter")
    print("5. Välju")

    valik = input("Sisestage valiku number: ")

    if valik == "5":
        print("Programm suletud.")
        break


    if valik == "1":
            kuup_kylg = float(input("Sisestage kuupi külg: "))
            ruumala = kuup_kylg ** 3
    elif valik == "2":
             = map(float, input("Sisestage kera raadiuse: "))
            ruumala = round((4*math.pi*r**3)/3,2)
    elif valik == "3":
             input("Sisestage silindri raadius ja kõrgus (eraldatud tühikutega): ").split())
            ruumala = math.pi * raadius**2 * korgus
    elif valik == "4":
            ristkulje_pikkus, korgus = map(float, input("Sisestage kuupirni ristkulje pikkus ja kõrgus (eraldatud tühikutega): ").split())
            ruumala = (1/3) * ristkulje_pikkus ** 3 + math.pi * (ristkulje_pikkus / 2) ** 2 * (korgus - ristkulje_pikkus / 2)
    else:
        print("Vigane valik. Palun proovige uuesti.")

        print(f"Kujundi ruumala on {ruumala} ühikut kuupühikut.")
    except ValueError:
        print("Vigane sisend. Palun sisestage numbriline väärtus.")


