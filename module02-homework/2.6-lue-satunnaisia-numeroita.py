import random

kolme_numeroa = ""
for i in range(3):
  kolme_numeroa += str(random.randint(0, 9))

nelja_numeroa = ""
for i in range(4):
  nelja_numeroa += str(random.randint(1, 6))

print(kolme_numeroa+"\n"+nelja_numeroa)