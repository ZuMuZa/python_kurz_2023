#https://kodim.cz/kurzy/uvod-do-progr-2/bonusy/cykly-2/excs  tombola

"""V tombole bylo prodáno celkem 1000 lístků. 
Naším úkolem je vylosovat náhodně tři výherce. 
Napište program, který vygeneruje a vypíše tři čísla mezi 1 a 1000. 
Využijte funkci randint, nezapomeňte ale, že si ji musíte importovat z modulu random.
Neřešte, že jedno číslo může být vygenerováno dvakrát."""

import random
pocet_vyhercu = 3
#print(list(range(pocet_vyhercu)))
for slosování in range(pocet_vyhercu):  
    print(f"Při slosování {slosování+1} byl vylosován lístek číslo {random.randint(1,1000)}")


"""Vypišme si čísla z nějakého rozsahu na základě jejich dělitelnosti dvěma čísly.
Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 3 i 4 současně.
Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 5 nebo 6. Stačí vypsat text: "Číslo je dělitelné 5 nebo 6." """

for x in range(50):
    if x % 3 == 0 and x % 4 == 0:
        print(f"cislo {x} je delitelne tremi i ctyrmi")
# to samy pak pro pet a sest, akorat namisto and tam bude or...

"""3_ 
Vraťte se k příkladu se zadáváním seznamu hostu na párty 
a zkopírujte si kód k sobě do editoru. 
Upravte program tak, že pokud uživatel v průběhu zadávání jmen napíše "konec", 
cyklus na zadávání jmen se ukončí."""

number_of_guests = int(input("zadej počet hostů: "))
guest_list = []
for i in range(number_of_guests):
    new_guest = input("Zadej jmeno hosta: ")
    if new_guest == "konec":
        break
    guest_list.append(new_guest)
print(guest_list)


"""4
Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo prvočíslo.

Prvočíslo je číslo, které je dělitelné beze zbytku pouze 2 čísly - 1 a sebou samotným.

Například 5 je prvočíslo, protože je dělitelná pouze 1 a 5.
Naopak 4 není prvočíslo, protože je dělitelná 1, 2 a 4."""

#cislo = int(input("Zadej cislo: "))

#prvocislo
#for x in range(2, cislo):
 #   if cislo % 1:
