import re

regularni_vyraz = re.compile(r"[a-z]{1,8}")
vstup = input("Zadej uživatelské jméno: ")
hledani = regularni_vyraz.fullmatch(vstup)
if hledani:
    print("Uživatelské jméno je v pořádku!")
else:
    print("Nesprávné uživatelské jméno!")



# pavla M.
"""
import re

regularni_vyraz = re.compile(r"[a-z]{1,8}")

uzivatelske_jmeno = input("Zadej uživatelského jména: ")
vysledek = regularni_vyraz.fullmatch(uzivatelske_jmeno)

if vysledek:
    print("Uživatelské jméno je v pořádku.")
else:
    print("Uživatelské jméno nesplňuje požadavky")
"""