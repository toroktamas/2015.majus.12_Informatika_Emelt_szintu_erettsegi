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
def szame(szo,karaktersorozat):
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
    if a["nap"] == 1:
        statisztika[1]+=1
    elif a['nap'] == 2:
        statisztika[2]+=1
    elif a['nap'] == 3:
        statisztika[3]+=1
    elif a['nap'] == 4:
        statisztika[4]+=1
    elif a['nap'] == 5:
        statisztika[5]+=1
    elif a['nap'] == 6:
        statisztika[6]+=1
    elif a['nap'] == 7:
        statisztika[7]+=1
    elif a['nap'] == 8:
        statisztika[8]+=1
    elif a['nap'] == 9:
        statisztika[9]+=1
    elif a['nap'] == 10:
        statisztika[10]+=1
    elif a['nap'] == 11:
        statisztika[11]+=1
    
for k, v in sorted(statisztika.items()):
    print("{0}. nap: {1} radioamator".format(k,v))

print("5. feladat")
"""Uzenet ossze rostalas."""
napok = []
n = 0
uj = []
for a in sorted(adas.values(), key=lambda a:a["azonosito"]):
    n+=1
    if a['nap'] == 1 and n == 1:
        for d in a["uzenet szovege"]:
            napok.append(d)
        
for di in a['uzenet szovege']:
    for f in napok:
        if di == f:
            pass
        if di!= f and f != "#":
            uj.append(f)
            
#print(napok)
#print(" ".join(uj))
#print("6. feladat")
"""fugveny keszites fent megoldottam """
print("7. feladat")
"""Bekeres es kiiratas."""
nap_bekeres = int(input("Adja meg a nap sorszamat! "))
radioamator_bekeres = int(input("Adja meg a radioamator sorszamat! "))


