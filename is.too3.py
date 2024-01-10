#Jarno Orusalu
#18.12.2023

#Ülikooli vastuvõetud
fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:

    vastuvõetud.append(int(rida))

#print(vastuvõetud)

aasta = 2019
print(f"Aastal {aasta} võeti vastu {vastuvõetud[aasta-2011]}õpilast")

fail.close()


#Sissetulekud
"""
Failis konto.txt on kirjas ujukomaarvudena pangakonto tehingud (kus positiivsed arvud on sissetulekud ja negatiivsed arvud on väljaminekud). Iga arv on eraldi real. Tekstifaili kasutamiseks programmi sees peab fail asuma programmifailiga samas kaustas.
Koostada programm, mis
loeb failist nimega konto.txt andmed;
väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud. Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks nagu failis. 
Näide programmi tööst:
Näiteks antud näitefaili konto.txt puhul peab ekraanile ilmuma
"""

fail = open("konto.txt", encoding="UTF-8")
for rida in fail:
    if float(rida) > 0:
        print(float(rida))


fail.close()