print ("Vítejte v dlouhodobém kurzu Pythonu!") # retezec, string, str

nazev_hry = "Romeo a Julie"
cena_listku = 150 #integer int
#pocet_listku = 5
##pocet_listku = int(input("Zadej počet lístků: "))
kupujici_vek = int(input("Prosím zadejte kolik je Vám let: "))

##celkova_cena = cena_listku * pocet_listku

# print(f"Cena všech lístku je {celkova_cena}")
#print("Cena všech lístku je", celkova_cena)

##if pocet_listku >= 3:
##    zlevnena_cena = celkova_cena * 0.9 #důležité je deklarovat novou proměnnou
##    print(f"Zlevněná cena je {zlevnena_cena}")
##else:
##    print(f"Cena všech lístků je {celkova_cena}")

if kupujici_vek >= 13:
    pocet_listku = int(input("Zadej počet lístků: "))
    celkova_cena = cena_listku * pocet_listku

    if pocet_listku >= 3:
        akce = pocet_listku - 1
        zlevnena_cena = akce * cena_listku
        print(f"Cena všech lístku je {zlevnena_cena}")
    else:
        print(f"Cena všech lístku je {celkova_cena}")
else:
    print("Bohužel Váš věk je příliš nízký pro nákup lístků.")
#    print(f"Zlevněná cena je {zlevnena_cena}")
#else:
#    print(f"Cena všech lístků je {celkova_cena}")