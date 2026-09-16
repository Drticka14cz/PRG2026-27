import random
import json
import tkinter
with open("H:\programovani25\PRG_4.G\liny_ucitel\zaci.json", "r", encoding="utf-8") as f:
    zaci = json.load(f)
    print(f"Loadnuto: {zaci}")



nahodna_znamka = random.randint(1,5)
print(nahodna_znamka)
zak = input("čí to bude známka?")

# zaci = {
#     "radek": 5,

# }
def zapsat_1(pridat):
    if pridat == "ano":
        # zaci.update({zak.append(nahodna_znamka)})
        zaci[zak].append(nahodna_znamka)
        print(zaci)
        with open("H:\programovani25\PRG_4.G\liny_ucitel\zaci.json", "w", encoding="utf-8") as f:
            json.dump(zaci, f, ensure_ascii=False, indent = 4)
            print("uloženo")
    else: 
        pass
def zapsat_2(pridat):
    if pridat == "ano":
        zaci.update({zak: [nahodna_znamka]})
        # zaci[zak].append(nahodna_znamka)
        print(zaci)
        with open("H:\programovani25\PRG_4.G\liny_ucitel\zaci.json", "w", encoding="utf-8") as f:
            json.dump(zaci, f, ensure_ascii=False, indent = 4)
            print("uloženo")
    else: 
        pass
if zak == "mohamed":
    nahodna_znamka = int(input("jaká bude mohamedova známka?"))
    pridat = input("Mámn tohoto žáka přidat do seznamu? ano/ne       ")
    if not zak in zaci:
        zapsat_2(pridat)
    else:
        zapsat_1(pridat)
elif not zak in zaci:
    pridat = input("Mámn tohoto žáka přidat do seznamu? ano/ne       ")
    zapsat_2(pridat)

elif zak in zaci:
    if zaci[zak] == nahodna_znamka:
        # print(f"Žák {zak} má již tuto známku({nahodna_znamka})")
        pridat = input("Mámn tohoto žáka přidat do seznamu? ano/ne       ")
        zapsat_1(pridat)

    else:
        # print(f"Snažíte se přidělit žákovi {zak} znamku {nahodna_znamka} přestože již má {zaci[zak]}")
        pridat = input("Mámn tohoto žáka přidat do seznamu? ano/ne       ")
        zapsat_1(pridat)
else:
    print("Spadly bakaláře")

prumer = zaci[zak]
soucet = 0
pocet = 0
for i in prumer:
    print(prumer)
    soucet += i
    pocet +=1
vysledek = soucet/pocet
if vysledek >3:
    print("smutné")
print(f"vysledek je: {vysledek}")











