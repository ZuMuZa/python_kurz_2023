import re

regularni_vyraz = re.compile(r"\w*\.?\w+@\w+\.cz")
email = input("Zadej e-mail: ")
hledani = regularni_vyraz.fullmatch(email)
if hledani:
    print("E-mail je v pořádku!")
else:
    print("Nesprávný e-mail!")



#Pavla Morávková
"""
regularni_vyraz = re.compile(r"\w+\.\w+@\w+\.cz")
email = input("zadej email: ")
vysledek = regularni_vyraz.fullmatch(email)

if vysledek:
    print("E-mail jméno je v pořádku.")
"""