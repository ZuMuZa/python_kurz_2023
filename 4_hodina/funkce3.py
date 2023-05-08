
def eur_to_czk (pocet_eur, kurz):
    """
    Funkce na převod eur do korun.
    bere dva parametry - počet eur, Kurz. 
    Vratí kolik stoji eura v korunách.
    """
    # víceřádkový komentář je u fce vlastně dokumentací která se u fce objeví po najetí kurzorem
    kurz = 25 #lokální proměnná - není vidět mimo fce
    pocet_czk = pocet_eur * kurz
    return pocet_czk


eura_uzivatel = int(input("kolik si přejete směnit euro?"))
print (eur_to_czk(eura_uzivatel, 25))  #definujeme zde že parametr kurz je a argument 25,,, eura_uzivatel se zapisuje do pocet_eur a 25 do kurz v def fce

#Nahrazení nahoře
#def eur_to_czk (pocet_eur, kurz=25):
#
#print (eur_to_czk(eura_uzivatel))
#
#nebo
#print (eur_to_czk(eura_uzivatel, 28))

print (eur_to_czk(pocet_eur = eura_uzivatel, kurz =28)) #vpořadí
print (eur_to_czk( kurz =28,pocet_eur = eura_uzivatel)) #při přehození pořadí, je důležité dodržet definici název=....
#print (eur_to_czk(pocet_eur = eura_uzivatel, 28)) # nefunguje - problém při kombinaci způsobu definicí
#print (eur_to_czk(eura_uzivatel, kurz =28,....=..., ...=...)) #první lze bez rovnítka daší už vždy s rovnítkem
