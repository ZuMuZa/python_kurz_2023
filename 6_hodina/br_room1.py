import re

regularni_vyraz = re.compile(r"[a-z]{1,8}")
vstup = input("Zadej uživatelské jméno: ")
hledani = regularni_vyraz.fullmatch(vstup)
if hledani:
    print("Uživatelské jméno je v pořádku!")
else:
    print("Nesprávné uživatelské jméno!")