#Jarno orusalu
#10.01.2024


#bänner
def banner(l):
    print(l.upper())


kord = int(input("Mitu korda: "))
tekst = input("Lisa tekst: ")


for i in range(kord):
    banner(tekst)

#Õunamahla tegemine 


def mahlapakkide_arv(kg):
    mahlapakkidearv = round(kg * 0.4 / 3)
    return mahlapakkidearv


kg = float(input("Sisesta õunte kogus: "))
print(mahlapakkide_arv(kg))








