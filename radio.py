#!/usr/bin/pithon3
# -*- coding:utf-8 -*-
"""2015.majus.12 Informatika emelt szintu erettsegi megoldas python programozasi nyelven."""
print("1. feladat")
"""Fajl beolvasa a veetel.txt alomanybol. amit en szotarral oldanak meg ami igy nezne ki.
adas={
azonosito{
"azonosito":nap*1000+radioamator sor szama
"nap":1-11 ig a napok szam
"radioamator sorszama":1-20 ig a radioamator sorszama
"uzenet szovege":
"hany farkast lattak":
 }
}
"""
def szame(szo):
    valasz = True
    for a in range(1,len(szo)):
        if szo[a]<"0" or szo[a]>'9':
            valasz = False
    return valasz

adas = {}
n=0
g=0
with open("veetel.txt", "rt", encoding="utf-8") as f:
    for s in f:
        g+=1
        sor = s.replace("\n", "")
        if g % 2 != 0:
            n+=1
            sor2 = sor.split(" ")
            adas[n] = {}
            adas[n]["nap"] = int(sor2[0])
            adas[n]["radioamator sorszama"] = sor2[1]
            adas[n]["azonosito"] = (int(sor2[0])*1000)+int(sor2[1])
        elif g%2 ==0:
            adas[n]["uzenet szovege"] = sor
            sor3 = sor.replace("#", "").split(" ")
            adas[n]["megfigyelt"] = sor3[0]

with open("sem.txt","wt", encoding="utf-8") as h:
    for k, v in adas.items():
        h.write("{0}:{1}\n".format(k,v))
#print(adas)
print("2. feladat")
"""Allomanyban szereplo elso es utolso uzenetet melyik radioamator rogzitatte."""
print("Az elso uzenetet rogzitoje: {0}\nAz utolso uzenet rogzitoje: {1}".format(adas[1]["radioamator sorszama"], adas[len(adas)]["radioamator sorszama"]))
print("3. feladat")
"""Meg kell adni azokat a feljegyzett napkat es azt hogy ki jegyezte fel amikor az uzenet szovegeben benne volt a "farkas" karaktersorozat. """
n=0
for a in adas.values():
    n+=1
    if "farkas" in a["uzenet szovege"]:
        print("{0}. nap {1} radioamator".format(a['nap'],a['radioamator sorszama']))


print("4. feladat")
"""statisztikat kell kesziteni hogymelyik nepon hany radioamator keszitett feljegyzest."""
statisztika={
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0
}
for a in adas.values():
    statisztika[a["nap"]] += 1

for k, v in sorted(statisztika.items()):
    print("{0}. nap: {1} radioamator".format(k,v))

print("5. feladat")
"""Uzenet ossze rostalas."""

uzenetek = {}
for nap in range(1,12):
    uzenet = ''  # ebben taroljuk majd az uzenete ahogy azt alakitjuk
    for v in adas.values():
        if v['nap'] == nap:
            if uzenet == '':
                uzenet = list(v['uzenet szovege'])
            else:
                # itt most vegig kell menni az uzeneten karakterenkent es megnezni, hogy
                # a mar az 'uzenet'-ben levo uzenet adott karakteren # van-e, mert ha igen, de az uj
                # uzenetben nem # es nem $ van, akkor azt a karaktert fogjuk beirni az 'uzenet'
                # adott helyere
                for k, b in enumerate(v['uzenet szovege']):
                    if uzenet[k] == '#' and b != '#' and b != '$':
                        uzenet[k] = b
    
    # most eltaroljuk a mar osszeallitott uzenet az uzenetek szotarban
    uzenetek[nap] = ''.join(uzenet)

with open("adaas.txt", "wt", encoding="utf-8") as f:
    for k in sorted(uzenetek):
        f.write(uzenetek[k]+'\n')

#print(" ".join(uj))
#print("6. feladat")
"""fugveny keszites fent megoldottam """
print("7. feladat")
"""Bekeres es kiiratas."""
nap_bekeres = int(input("Adja meg a nap sorszamat! "))
radioamator_bekeres = int(input("Adja meg a radioamator sorszamat! "))

# eloszor dontsuk el hogy az adott radioamator dolgozott-e aznap, mert kulonben azt kell kiirni,
# hogy "Nincs ilyen megfigyeles"
dolgozott = False
for v in adas.values():
    if v['nap'] == nap_bekeres and int(v['radioamator sorszama']) == radioamator_bekeres:
        dolgozott = True

if not dolgozott:
    print("Nincs ilyen megfigyeles")
else:  # ha dolgozott az adott radioamator, akkor vegyuk ki a megfigyelesek szamat a helyreallitott szovegbol
    megfigyelesek = uzenetek[nap_bekeres].split(' ')[0].split('/')
    megfigyelheto = False  # volt-e megfigyeles aznap
    megfigyelt = 0  # egyedek szama
    if 0 in megfigyelesek and szame(megfigyelesek[0]):
        megfigyelheto = True
        megfigyelt += int(megfigyelesek[0])
    if 0 in megfigyelesek and szame(megfigyelesek[1]):
        megfigyelheto = True
        megfigyelt += int(megfigyelesek[1])

    if not megfigyelheto:
        print("Nincs informacio")
    else:
        print("A megfigyelt egyedek szama: {0}".format(megfigyelt))
    
        