# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

minValue = None
maxValue = None

while True:
  numeroString = input("Anna numero: ")
  if numeroString == "": break

  numeroInt = int(numeroString)
  if minValue == None or minValue > numeroInt:
    minValue = numeroInt
  if maxValue == None or maxValue < numeroInt:
    maxValue = numeroInt

if minValue == None: print("Ei lukuja syötetty.")
else: print(f"Pienin numero on {minValue} ja suurin numero on {maxValue}.")