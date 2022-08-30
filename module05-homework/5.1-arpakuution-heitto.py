# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
# Käytä for-toistorakennetta.

import random

diceCount = int(input("Montako arpakuutioa heitetään? "))
listOfDice = []

for i in range(diceCount):
  dice = random.randint(1, 6)
  listOfDice.append(dice)

print(sum(listOfDice))