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
adas = {}
n=0
with open("veetel.txt", "rt", encoding="utf-8") as f:
    for s in f:
        n+=1
        sor = s.replace("\n", "").split(" ")
        adas[n] = {}
        if n % 2 != 0:
            adas[n]["nap"] = sor[0]
            adas[n]["radioamator sorszama"] = sor[1]
            adas[n]["azonosito"] = (int(sor[0])*1000)+int(sor[1])
        else:
            adas[n]["uzenet szovege"] = sor[1:]
            sor2 = sor[0].split("/")
            adas[n]["farkas felnott"] = sor2[0]
            adas[n]["farkas gyerek"] = sor2[1]

with open("sem.txt","wt", encoding="utf-8") as h:
    for k, v in adas.items():
        h.write("{0}:{1}\n".format(k,v))            
print("2. feladat")
""" """
print("3. feladat")
""" """
print("4. feladat")
""" """
print("5. feladat")
""" """
print("6. feladat")
""" """
print("7. feladat")
""" """
print("8. feladat")
""" """

