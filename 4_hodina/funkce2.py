# globální proměnná velkými písmeny
KURZ = 25 


def eur_to_czk (pocet_eur):
    """
    Funkce na převod eur do korun.
    bere jeden parametr - počet eur. Kurz fixní 25 korun za 1 euro.
    Vratí kolik stoji eura v korunách.
    """
    # víceřádkový komentář je u fce vlastně dokumentací která se u fce objeví po najetí kurzorem
    kurz = 25 #lokální proměnná - není vidět mimo fce
    pocet_czk = pocet_eur * KURZ
    return pocet_czk


eura_uzivatel = int(input("kolik si přejete směnit euro?"))
print (eur_to_czk(eura_uzivatel))

#print(kurz)  #proměnná kurz mimo tělo fce neexistuje tudíž by to bylo chybně a nefungoval by print
print (KURZ)