# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

vastaus = random.randint(1, 10)

while True:
  arvaus = int(input("Arvaa luku: "))
  
  if arvaus == vastaus:
    print("Oikein!")
    break
  elif arvaus < vastaus:
    print("Liian pieni arvaus.")
  else:
    print("Liian suuri arvaus.")