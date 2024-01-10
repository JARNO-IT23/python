#J_0rusalus
#05.12.2023

fail = open ("s6pru_l6ustaraamatus.txt", "r")
re = 0
ke = 0
erakonnd = []
sisu = fail.readlines()
for tyyp in sisu:
    print(tyyp,end="")
    tyybike = tyyp.split(" ")
    if tyybike[2]=="RE":
        re = re+1 
    elif tyybike[2]=="KE":
        ke = ke+1 
    if tyybike[2] not in erakonnd:
        erakonnd.append(tyybike[2])
    with open("poliitikud.txt", "a") as uusfail:
        uusfail.write(tyybike[0]+" "+tyybike[2]+"\n")

