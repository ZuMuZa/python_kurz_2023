"""Vytvořte seznam, který obsahuje

každé z čísel ze seznamu cisla vynásobené dvěma,
každé z čísel ze seznamu cisla s opačným znaménkem,
každé z čísel ze seznamu cisla umocněné na druhou,
každé z čísel ze seznamu cisla jako řetězec."""


cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
cisla_2x = [x*2 for x in cisla] 
print(cisla_2x)
cisla_2x = [x*(-1) for x in cisla] 
print(cisla_2x)
cisla_2x = [x**2 for x in cisla] 
print(cisla_2x)
cisla_2x = [str(x) for x in cisla] 
print(cisla_2x)


"""Vytvořte seznam, který obsahuje

počty písmen ve všech jménech,
všechna jména napsaná velkými písmeny,
všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména),
všechna jména převedená na malá písmena s koncovkou '@email.cz'."""


jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
print(f"pocet pismen je: {[len(x)for x in jmena]}")
print(f"Všechna velkými {[jmeno.upper() for jmeno in jmena]}")
print(f"ženská jmena {[jmeno + 'a' for jmeno in jmena]}")
print(f"ženská jmena {[jmeno.lower() + '@email.cz' for jmeno in jmena]}")
email =[jmeno.lower() + '@email.cz' for jmeno in jmena]
print(f" A ještě podruhé {email}")
#print(f"pocet pismen je: {[str(x)+'a' for x in jmena]}")


#ad ukol 3
#průměrná vymysli
#ranní návod:
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
ranni_teploty = [teplota[0] for  teplota in teploty]
print(ranni_teploty)
