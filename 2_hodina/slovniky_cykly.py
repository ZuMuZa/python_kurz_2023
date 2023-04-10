sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for kniha in sales:
    print(kniha)
###2### obdobné jako níže
print(f"kniha  s nazvem{kniha} se prodalo {sales[kniha]}ks.")


tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

for listek in tombola:
    print(f"listek {listek} vyhrava {tombola[listek]} ks.")


#JAKÉ JSOU KLÍCE VE slOVNIKU
    print(sales.keys())
#jaké hodnoty jsou ve slovníku
    print(sales.values())

#kolik se průměrně prodalo výtisku
print(sum(sales.values())/len(sales))

#metoda item ###2### obdobné jako výše
print(sales.items())
for nazev, prodano in sales.items():
    print(f"knihy s nazvem {nazev} se prodalo {prodano} ks.")