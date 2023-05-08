a=5
b=7

#print(a+b)

def secti(l,k): #a,b parametry
    return l+k #vrátí sečtení pokud zadám jen l+k bez "return" tak fce nic nevrátí (none) na řádku 13 vysledek a ř.14  print,,,, print(return 8+5) taky nebude fungovat, return funguje jen ve fci

secti(8,5) #8,5 argumenty
# fce musí být nejdříve definovana a pak ji lze volat

#print(l, k)   l, k nejsou mimo funkci secti videt a tak to nic nevytiskne

vysledek = secti(8,5)
print(f"vysledek je: {vysledek}")

# ke kazdému cislu v seznamu přičti 1 pomocí fce secti
seznam_cisel = [2,5,9,8]

#vysledek jen vypiseme
for cislo in seznam_cisel:
    print(secti(cislo,1))

#vysledek uložíme do nového seznamu
soucty = []
for cislo in seznam_cisel:
    soucty.append(secti(cislo,1))  #append přidá číslo do nového seznamu
print(soucty) # nebo seznam_cisel = soucty   #přepíše původní seznam

"""nebo lze
def secti(l,k): #a,b parametry
    soucet_a = l+k
    return soucet_a
    """
