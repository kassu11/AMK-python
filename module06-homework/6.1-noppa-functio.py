# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def dice():
  return random.randint(1, 6)

diceNumber = None

while diceNumber != 6:
  diceNumber = dice()
  print(f"Heitettiin nopalla: {diceNumber}")