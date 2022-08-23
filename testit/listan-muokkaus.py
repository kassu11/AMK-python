from functools import reduce


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def muutin(x):
  return "{} t".format(x)

tulos = map(lambda x: "{} ad".format(x), lista)
tulos = map(muutin, lista) # Sama asia
print(list(tulos))

tulos = filter(lambda x: x == 4, lista)
print(list(tulos))

tulos = reduce(lambda v, acc: str(acc) + str(v), lista)
print(list(tulos))