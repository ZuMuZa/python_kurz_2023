import re
#vytvoření regulárního výrazu
regularni_vyraz = re.compile(r"(\+420)? ?\d{3} ?\d{3} ?\d{3}")

vstup = input("Zadej tel. číslo: ")

vstup_ok = regularni_vyraz.fullmatch(vstup)

if vstup_ok:
    print("Tel.číslo je v pořádku")
else: 
    print("Nesprávné tel. číslo")


