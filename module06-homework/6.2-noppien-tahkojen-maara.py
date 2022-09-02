# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def dice(sides):
  return random.randint(1, sides)

numberOfSides = int(input("Kirjoita nopan tahkojen määrä: "))
numberOfDice = None

while numberOfDice != numberOfSides:
  numberOfDice = dice(numberOfSides)
  print(f"Heitettiin nopalla: {numberOfDice}")