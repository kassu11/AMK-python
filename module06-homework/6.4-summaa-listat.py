# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa listassa olevien lukujen summan. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

import random
numbers = []

def sum2(numberList):
  return sum(numberList)

for i in range(5):
  numbers = []
  for length in range(5):
    numbers.append(random.randint(1, 100))
  print(f"\nLista: {numbers} \nSumma: {sum2(numbers)}")
