#Python1 - 7_hodina- (Třídy a dědičnost) - ukol 07 - Zuzka Musilová
#ZADÁNÍ:

"""

Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	        Peugeot 403 Cabrio	    47534
1P3 4747	        Škoda Octavia	        41253
Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

registrační značka automobilu registracni_znacka,
značka a typ vozidla typ_vozidla,
počet najetých kilometrů najete_km,
informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy volné.

Vytvoř objekty, které reprezentují oba automobily půjčovny.

Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát.
"""

#ŘEŠENÍ:
from dataclasses import dataclass

@dataclass
class Auto:
    registracni_znacka: int
    typ_vozidla: str
    najete_km: int
    dostupnost: bool   #True = volné, False = vypůjčené
        

    def pujc_auto(self):
        if self.dostupnost is True:
            self.dostupnost = False                           
            return f"Potvrzuji zapůjčení vozidla"           
        else:
            return f"Vozidlo není k dispozici"    

    def __str__(self) -> str:
        return f"Auto {self.typ_vozidla} má registrační značku: {self.registracni_znacka} a jeho dostupnost je {self.dostupnost}."

    def get_info(self) -> str:
        return f"Auto {self.typ_vozidla} má registrační značku: {self.registracni_znacka}."
    
    def vrat_auto(self, tachometr_pri_vraceni, kolik_dni_pujceno):       
        self.najete_km = tachometr_pri_vraceni
        self.dostupnost = True
        self.kolik_dni_pujceno = kolik_dni_pujceno
        self.cena_pujceni = 0
        if self.kolik_dni_pujceno < 7:
            self.cena_pujceni = self.kolik_dni_pujceno * 400
            return f"Za zapůjčení auta {self.typ_vozidla} na {self.kolik_dni_pujceno} dní, zaplatíte {self.cena_pujceni} Kč."
        elif self.kolik_dni_pujceno >= 7:
            self.cena_pujceni = self.kolik_dni_pujceno * 300
            return f"Za zapůjčení auta {self.typ_vozidla} na {self.kolik_dni_pujceno} dní, zaplatíte {self.cena_pujceni} Kč."
        else:
            return f"Chyba v počtu dní, během kterých bylo auto zapůjčeno."
            

A1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
A2 = Auto("1P3 4747", "Škoda Octavia", 41253, False)
A3 = Auto("-", "-", 0, True) # pro rozšíření vozového parku půjčovny :)


#print(A1)
#print(A1.pujc_auto())
#print(A1)   

vstup = int(input("Zadejte značku auta, kterou si chcete půjčit. Zadání proveďte napsáním '1' jako Peugeot nebo '2' jako Škoda: "))
if vstup == 1:
    #print(A1)
    print(A1.get_info())
    print(A1.pujc_auto())
    #print(A1)
elif vstup == 2:
    #print(A2)
    print(A2.get_info())
    print(A2.pujc_auto())
    #print(A2)
else: 
    print("Neplatný výběr auta")

tachometr = int(input("Zadejte stav tachometru při vrácení: "))
dny_zapujceni = int(input("Zadejte kolik dní bylo auto zapůjčeno: "))
print(A2.vrat_auto(tachometr, dny_zapujceni))

# Děkuji za kontrolu a přeji hezký den :-)
# Zuzka