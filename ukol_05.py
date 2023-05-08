#Python1 - 5_hodina- (Typování funkcí, Cykly 2: list comprehension, dict comprehension) - ukol 05 - Zuzka Musilová
#ZADÁNÍ:

"""
Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
"""
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
"""
1. Vytvoř seznam průměrných teplot pro každý den.
2. Vytvoř seznam ranních teplot.
3. Vytvoř seznam nočních teplot.
4. Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
"""

#ŘEŠENÍ:

#1.
print("1. část",22*"+")
sez_prumerne_teploty = []
for teplota in teploty:
    prumerne_teploty = round(sum(teplota[0:])/len(teplota[0:]),1)
    #print(prumerne_teploty)
    sez_prumerne_teploty.append(prumerne_teploty)
    
print("Seznam průměrných teplot pro každý den:")
print(sez_prumerne_teploty)
print("konec 1. části",15*"-")
print(" ")

#2.
print("2. část",22*"+")
ranni_teploty = [teplota[0] for  teplota in teploty]
print("Seznam ranních teplot v týdnu:")
print(ranni_teploty)
a=0
b=0
for teplota in ranni_teploty:
    a = a + teplota
    b = b+1
    #print(a)
    #print(b)

#print(a/b)  
c= round((a/b),1) 
print(f"Průměrná ranní teplota během týdne byla {c}°C.")
print("konec 2. části",15*"-")
print(" ")

#3.
print("3. část",22*"+")
nocni_teploty = [teplota[3] for  teplota in teploty]
print("Seznam nočních teplot v týdnu:")
print(nocni_teploty)
print("konec 3. části",15*"-")
print(" ")

#4.
print("4. část",22*"+")
#poledni_nocni_teploty = []
tydenni_seznam = []
for teplota in teploty:
    poledni_nocni_teploty = []
    poledni_nocni_teploty.insert(0,teplota[1])
    poledni_nocni_teploty.insert(1,teplota[3])
    tydenni_seznam.append(poledni_nocni_teploty)
#poledni_nocni_teploty.append(teplota[3])
print("Seznam poledních a nočních teplot pro každý den v týdnu:")
#print(poledni_nocni_teploty)
print(tydenni_seznam)
print("konec 4. části",15*"-")
print(" ")

# Děkuji za kontrolu a přeji hezký den :-)
# Zuzka