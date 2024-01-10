#Jarno Orusalu 
#18.12.2023

#Tervitus
print("Tere, maailm!")


"""
Koostada programm, mille;
1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks &quot;teelehe-
mosaiikliblikas&quot; (sõnena);
●3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks &quot;. aasta
liblikas on &quot; (sõnena);
4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks
sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni,
mis teisendab arvu sõneks);
5. real väljastatakse muutuja lause väärtus ekraanile.
"""

aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)

"""
Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi
pilvedeks. Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel,
alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
● küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
● väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
● väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.
"""
korgus = float(input("Sisesta pilvede aluse kõrgus kilomeetrites : "))

if korgus > 6.0:
    print("Need on ülemised pilved.")
else:
    print("Need ei ole ülemised pilved.")

"""
Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid
on vähemalt üks. Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi
kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu
inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).
Võib-olla on abi nendest tehetest
● // täisarvuline jagamine, 36 // 10 → 3
● % jäägi leidmine 36 % 10 → 6
Testige oma programmi muuhulgas järgmiste algandmetega:
● inimeste arv: 60, kohtade arv: 40;
● inimeste arv: 80, kohtade arv: 40;
● inimeste arv: 20, kohtade arv: 40;
● inimeste arv: 40, kohtade arv: 40.
Püüdke ka mõista, miks just sellised testandmed valiti.
"""

inimeste_arv = int(input("Sisesta inimeste arv: "))
kohtade_arv_uhes_bussis = int(input("Sisesta ühe bussi kohtade arv: "))

busside_arv = inimeste_arv // kohtade_arv_uhes_bussis


viimase_bussi_inimesed = inimeste_arv % kohtade_arv_uhes_bussis


print(f"Vaja on {busside_arv} bussi.")
print(f"Viimases bussis on {viimase_bussi_inimesed} inimest.")
