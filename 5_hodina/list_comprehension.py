# chroustání seznamů = list comprehension

znamky = [0, 2, 0, 1, 1, 3] # znamkovaní programatoru

opravene_znamky = [] # bezne znamekovani (o 1 vetsí)
for znamka in znamky:
    opravene_znamky.append(znamka+1)
    # opravene_znamky = opravene_znamky + [znamka +1]

print(opravene_znamky)


#priklad 2 
kilometry = [2.4, 2.6, 0, 3.5, 1.8]

zaokrouhlene_kilometry = []
for zaznam in kilometry:
    zaokrouhlene_kilometry.append(round(zaznam))
    #zaokrouhlene_kilometry = zaokrouhlene_kiometry + [round(zaznam)]
print(zaokrouhlene_kilometry)


#priklad 1 pomocí list_comprehension
znamky = [0, 2, 0, 1, 1, 3] # znamkovaní programatoru

opravene_znamky = [znamka+1 for znamka in znamky] # modifikace x for x in původní seznam, není třeba fce append....takové zjednodušení
print(opravene_znamky)

# priklad 2 pomocí list comprehension
kilometry = [2.4, 2.6, 0, 3.5, 1.8]

zaokrouhlene_kilometry = [round(zaznam)for zaznam in kilometry]
print(zaokrouhlene_kilometry)

"""list comprehension je vhodný pro jednoduchou akci, ..přidej ke všem jsmenum @ ...také je to rychlé/optimalizované"""
""" .append je vhodné když to mám složité třeba s přistupováním k serveru, ..nebo if a elif.."""

znamky = [0, 2, 0, 1, 1, 3]
opravene_znamky = [znamka+1 if znamka <3 else znamka for znamka in znamky] 
print(opravene_znamky)

if znamka <3:
    opravene_znamky.append(znamka+1)
else:
    opravene_znamky.append(znamka)

def oprav_znamku (znamka: int) -> int:  #znamka je jen ve funkci uvnitř
    if znamka <3:
        return znamka + 1
    else:
        return znamka
    
opravene_znamky = [oprav_znamku(x) for x in znamky]
print(opravene_znamky)

opravene_znamky = [znamka+1 if znamka <3 or znamka<4 else znamka for znamka in znamky]   #lze and nebo or ale nelze ve zjednodušeném elif!
#lepší je ve složitějších případech (nečitelných) to rozhodit do fce a pak v comprehension volat fci   