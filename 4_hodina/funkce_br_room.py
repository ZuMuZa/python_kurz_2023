#Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

def mult(l,k):
    return l*k

vysledek = mult(8,5)
print(f"vysledek je: {vysledek}")

"""
Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).
"""
cena_za_noc = 850
cena_za_snidani = 125

#persons = int(input("kolik osob bude na noc v hotelu?")) 
#breakfast = input("Budete chtít snídani?")
"""
def total_price(persons, breakfast=False):
                If breakfast = True
            cena_noci = persons*(cena_za_noc+cena_za_snidani)
        else 
            cena_noci = persons*(cena_za_noc)
    return cena_noci
"""
"""
print(f"Cena noci je: {total_price(persons, breakfast)}") 
print(f"Cena noci je: {total_price(3)}") 
print(f"Cena noci je: {total_price(2,true)}") 
"""
"""
def total_price(persons, breakfast=False):
     price_for_person = cena_za_noc* persons

     price_for_breakfast_persons = 0
     if breakfast:
          price_for_breakfast_persons = cena_za_snidani*persons

    return price_for_person + price_for_breakfast_persons
"""
"""
pravda = True
nepravda = False
if pravda or nepravda:
    print("pravda")
if pravda and not nepravda:
    print("pravda")
#
Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

Zadej slovo: ahoj
********
* ahoj *
********
Nápověda: 8 * '*' == '********'

Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr.
"""
def print_v_ramecku():
     slovo = input("Zadej slovo:")
     print("*" * (len(slovo)+4))
     print(f"*{slovo} *")
     print("*" * (len(slovo)+4))