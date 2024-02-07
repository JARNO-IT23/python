#jarno Orusalu
#It23





"""
KaugushÃ¼pe
kasutaja sisestab 3 kaugushÃ¼ppe tulemust - 1p
sinu programm leiab ning vÃ¤ljastab parima ja keskmise tulemuse - 2p
programmi dialoog kasutajaga on arusaadav ja Ã¼heselt mÃµistetav - 1p
kood kommenteeritud - 1p
"""

print("......................Kaugushüppe Tulemused.........................")
tulemused = []
for i in range(3):
    tulemus = float(input(f"Sisesta {i + 1}. kaugushüppe tulemus: "))
    tulemused.append(tulemus)

parim = max(tulemused)
keskmine = sum(tulemused) / len(tulemused)
print(f"Parim tulemus: {parim}")
print(f"Keskmine tulemus: {keskmine}")

"""
Eurokalkulaator
Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vÃµi EEK->EUR.
Oluline on kasutada kahte funktsiooni!!
"""

def eur_to_eek(eur):
    return eur * 15.6466

def eek_to_eur(eek):
    return eek / 15.6466

print("......................Eurokalkulaator.........................")
print("1. EUR -> EEK")
print("2. EEK -> EUR")
valik = int(input("Vali tegevus: "))
if valik == 1:
    eur = float(input("Sisesta EUR summa: "))
    print(f"{eur} EUR on {eur_to_eek(eur)} EEK")    
elif valik == 2:
    eek = float(input("Sisesta EEK summa: "))
    print(f"{eek} EEK on {eek_to_eur(eek)} EUR")
else:
    print("Vigane valik")

"""
Palkade vÃµrdlus - Loo palk.txt fail tÃ¶Ã¶tajate nime, soo ja palganumbriga (10 tÃ¶Ã¶tajat).
Koosta programm, mis analÃ¼Ã¼sib kas firmas toimub diskrimineerimist soo jÃ¤rgi. Selleks vÃµrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kÃµige kÃµrgemat palka. Programm peab tegema otsuse.

Hubert Hunt m 2340
Siim Siil m 2570
MÃ¤rt MÃ¤ger m 1960
Vilma Vihmauss n 2060
Merike Metskits n 2250
Kati Karu n 2370
Elmar Elevant m 2900
Timoteus Tigu m 2850
Reet Rebane n 2340
Kalev Kaamel m 2570
Karmen Kass n 2120
Kornelius Koer m 2250
"""

print("......................Palkade Võrdlus.........................")
with open("palk.txt", "r", encoding="utf-8") as f:
    read = f.readlines()

meeste_palk = []
naiste_palk = []

for line in read:
    nimi, sugu, palk = line.split()
    palk = int(palk)
    if sugu == "m":
        meeste_palk.append(palk)
    else:
        naiste_palk.append(palk)

meeste_keskmine = sum(meeste_palk) / len(meeste_palk)
naiste_keskmine = sum(naiste_palk) / len(naiste_palk)
meeste_maksimum = max(meeste_palk)
naiste_maksimum = max(naiste_palk)









