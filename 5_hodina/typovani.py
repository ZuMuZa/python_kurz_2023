#def eur_to_czk(pocet_eur, kurz=25):   #předchozí neotypovaná fce
def eur_to_czk (pocet_eur: int, kurz: int=25) -> int:  #typování ": int"  urcuji rovnou co za datový typ mají mít parametry, "-> int" říká jaký dat.typ vrátí fce
    """
    Funkce na převod eur do korun.
    bere dva parametry - počet eur, Kurz. 
    Vratí kolik stoji eura v korunách.
    """
       
    pocet_czk = pocet_eur * kurz
    return pocet_czk

eura_uzivatel = int(input("Kolik si přejete směnit euro?"))
print(eur_to_czk(eura_uzivatel))