print("martin".upper())
print("MARTIN".lower())
print("  Mart in ".strip())
print("m a r t i n".split(" "))
print("+".join(["1","2","3","4"]))

text = "Kurz vede lektor Marek"
novy_text = text.replace("Marek", "Janka")
print(novy_text)


pohyby = [1200, -250, -800, 540, 721, -613, -222]
print(pohyby[2])
print(pohyby[2:])
print(len(pohyby))
print(min(pohyby))
print(max(pohyby))
print(sum(pohyby))
sorted_pohyby = sorted(pohyby)
print(sorted_pohyby[0],sorted_pohyby[6])

print(sum(pohyby)/len(pohyby))
import math