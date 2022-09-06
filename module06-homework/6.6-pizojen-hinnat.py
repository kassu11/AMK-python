# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). 
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

def calculatePizaPrice(diameter, price):
  squareCentimeter = diameter / 2 ** 2 * math.pi;
  squareMeter = squareCentimeter / 10000;
  return squareMeter * price

pizas = []

for i in ["A", "B"]:
  diameter = float(input(f"{i}). Anna pizzan halkaisija senttimetreinä: "))
  price = float(input(f"{i}). Anna pizzan hinta euroina: "))
  pizas.append(price)
  print(f"{i}). Yksikköhinta on: {calculatePizaPrice(diameter, price):.2f} €/m2\n")

if pizas[0] < pizas[1]:
  print("A). pizza on halvempi")
elif pizas[0] > pizas[1]:
  print("B). pizza on halvempi")
else:
  print("Pizzat ovat saman hintaiset")