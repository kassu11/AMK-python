# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

import random

def filterOddNumbers(numberList):
  return [number for number in numberList if number % 2 == 0]

for i in range(5):
  numbers = []
  for length in range(5):
    numbers.append(random.randint(1, 100))
  print(f"\nLista: {numbers} \nSumma: {filterOddNumbers(numbers)}")