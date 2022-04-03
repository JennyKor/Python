##Jenny Korkeamäki
import Kolmiot

print("Anna kolmion sivujen pituudet:")
sivu1 = float(input("1. sivu: "))
sivu2 = float(input("2. sivu: "))
sivu3 = float(input("3. sivu: "))

kolmio = Kolmiot.LueSivut(sivu1, sivu2, sivu3)
print("Kolmio on " + kolmio + ".")
