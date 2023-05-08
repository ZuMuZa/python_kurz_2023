import random

#cyklus pomocí číselné řady
jmena = ["Anna", "Adela", "Alena", "Adam"]

for jmeno in jmena:
    print(jmeno)

pocet_hracu = 4
hod_1 = random.randint(1,6)
hod_2 = random.randint(1,6)
hod_3 = random.randint(1,6)
hod_4 = random.randint(1,6)
#print(hod_1, hod_2, hod_3, hod_4)
# a co když bude hráčů 30, nebo 1000?

print(list(range(pocet_hracu))) # vrací interval od 0 do 4, vlastně možnost iterovat kolikrát určíme

#chceme tolikrát hodit kostkou kolik máme hráčů
for hrac in range(pocet_hracu):  #opakuj tolikrát, kolik zadáme parametr funkci range (zde pocet_hracu)
    print(random.randint(1,6))
    
for hrac in [1, 2, 3, 4]:  #nepraktický způsob pro vyšší počet hráčů
    print(random.randint(1,6))

for hrac in range(pocet_hracu):  #pojmenovaná proměnná kterou použijeme
    print(f"Hrac {hrac} hodil {random.randint(1,6)}") #s vypsáním jmen hráčů

for _ in range(pocet_hracu):  #nepojmenovaná proměnná kterou nepoužijeme
    print(f"Hrac hodil {random.randint(1,6)}") #bez vypsáním jmen

# slo by samozřejmě i "for hrac in jmena:"
#   print(f"Hrac {jmena[hrac]} hodil {random.randint(1,6)}")

# v podstatě je to generátor čísel tolik kolik potřebujeme

for _ in range(1,5):  #od 1 do 5, bez 5 ...tedy 1,2,3,4  ... do +1
    print(f"Hrac hodil {random.randint(1,6)}")