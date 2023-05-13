import re
#vytvoření regulárního výrazu
regularni_vyraz = re.compile(r"(\+420)? ?\d{3} ?\d{3} ?\d{3}")

vstup = input("Zadej tel. číslo: ")

vstup_ok = regularni_vyraz.fullmatch(vstup)

if vstup_ok:
    print("Tel.číslo je v pořádku")
else: 
    print("Nesprávné tel. číslo")


# https://regexcrossword.com/

#dalsi
"""
Přidej k regulárnímu výrazu na číslo účtu možnost předčíslí, tj. na začátku může být 0 až 6 čísel a za nimi může (ale nemusí) být pomlčka.
\d{0,6}-?\d{6,10}/\d{4}
Číslo účtu podruhé
[12][0-2]\d{6,8}/2100
Registrační značka
\d[A-Z]\w \d{4}
# vylepsene o kraje
\d(A|B|C|E|H|J|K|L|M|P|S|T|U|Z)\w \d{4}
nebo
\d[A, B, C, E, H, J, K, L, M, P, S, T, U, Z]\w \d{4}
Telefonní číslo
(\+420)? ?\d{3} ?\d{3} ?\d{3}
"""