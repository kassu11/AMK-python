import random


def create_lottery_row():
  lotto_string = ""
  for i in range(7):
    lotto_string += str(random.randint(1, 39))

  return lotto_string



print(create_lottery_row())

for i in range(5):
  print(i)

print("asdasd", i)

lista = [1,2,3,4,5,6,7,8,9,10]

for i in lista:
  if(i % 2 == 0): lista.remove(i)
  print("Lista", i)