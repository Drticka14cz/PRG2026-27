import random
import json

with open("H:\programovani25\PRG_4.G\liny_ucitel\zaci.json", "r", encoding="utf-8") as f:
    zaci = json.load(f)
    print(f"Loadnuto: {zaci}")



nahodna_znamka = random.randint(1,5)
print(nahodna_znamka)
zak = input("čí to bude známka?")

# zaci = {
#     "radek": 5,

# }
if not zak in zaci:
    pridat = input("Mámn tohoto žáka přidat do seznamu? ano/ne       ")
    if pridat == "ano":
        zaci.update({zak: nahodna_znamka})
        print(zaci)
        with open("H:\programovani25\PRG_4.G\liny_ucitel\zaci.json", "w", encoding="utf-8") as f:
            json.dump(zaci, f, ensure_ascii=False, indent = 4)
            print("uloženo")
    else: 
        pass

elif zak in zaci:
    if zaci[zak] == nahodna_znamka:
        print(f"Žák {zak} má již tuto známku({nahodna_znamka})")
    else:
        print(f"Snažíte se přidělit žákovi {zak} znamku {nahodna_znamka} přestože již má {zaci[zak]}")
else:
    print("Spadly bakaláře")










