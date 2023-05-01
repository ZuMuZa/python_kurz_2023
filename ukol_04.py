#Python1 - 4_hodina- (vlastní funkce) - ukol 04 - Zuzka Musilová
#ZADÁNÍ:

"""
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:

Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".
"""

#ŘEŠENÍ:


cislo_prijemce = input ("Zadejte prosím telefoní číslo, na které chcete odeslat SMS: ")

def overeni (cislo_prijemce: str)-> bool:
    """
    Funkce na ověření správného formátu u telefoního čísla zadaného uživatelem.
    bere jeden parametr - zadané telefonní číslo. 
    Vratí zda je číslo zadané ve správném formátu.
    """
    if len(cislo_prijemce) == 13 and cislo_prijemce[:4] == "+420":
        return True
        
    elif len(cislo_prijemce) == 9:
        return True
        
    else:
        return False
    


def cena_sms (sms_zprava: str)->int: 
    """
    Funkce na spočtení ceny sms zadané uživatelem.
    bere jeden parametr - zadaná sms zpráva. 
    Vratí cenu sms zprávy.
    """
    cena = ((len(sms_zprava)//180)+1) * 3
    return cena


if overeni(cislo_prijemce) == True:
    sms_zprava = input ("Zadejte prosím SMS zprávu, kterou chcete odeslat na Vámi zadané telefonní číslo: ")
    #print("Zpráva má", len(sms_zprava), "znaků.")
    print("Zpráva stojí", cena_sms(sms_zprava), "Kč")
else:
    print("Zadané číslo má špatný formát.")



# Děkuji za kontrolu a přeji hezký den :-)
# Zuzka