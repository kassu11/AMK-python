from math import floor

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: ")) + leiviska * 20
luoti = float(input("Anna luodit: ")) + naula * 32
gramma = luoti * 13.3
kilo = floor(gramma / 1000)

print("Massa nykymittojen mukaan: ")
print(f"{kilo} kilogrammaa ja {gramma % 1000:.2f} grammaa.")