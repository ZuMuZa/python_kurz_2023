
#slovníky - ukol 02 - Python1 - Zuzka Musilová
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
#vstupní informace od zákazníka
kod_soucastky = input ("Zadej kód součástky: ")
pocet_kusu = int(input ("Zadej počet kusů, které potřebuješ: "))

#kontrola stavu skladu a možnosti uspokojit poptávku zákazníka
if kod_soucastky in sklad:
    print (f"{kod_soucastky} Máme na skladu v množství {sklad[kod_soucastky]} kusů.")
    pocet_na_skladu = sklad[kod_soucastky]

    if pocet_kusu <= pocet_na_skladu:
        print("Součástek máme na skladu dostatek. Vaše poptávka bude uspokojena.")
        sklad[kod_soucastky] = sklad[kod_soucastky] - pocet_kusu
        print(sklad)
    else:
        print(f"Na skladu je pouze omezené množství součástek. Můžeme prodat {sklad[kod_soucastky]} Ks ")
        sklad.pop(kod_soucastky)
        print(sklad)
else:
    print("Bohužel tuto součástku na skladu nevedeme. Zkuste se domluvit s obsluhou na jejím zavedení na sklad.")