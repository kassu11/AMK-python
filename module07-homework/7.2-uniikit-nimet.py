# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä. 
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa, joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. 
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. 
# Käytä joukkotietorakennetta nimien tallentamiseen.

names = set()

while True:
  name = input("Kirjoita nimi: ")
  if name == "": break
  elif name in names:
    print("Aiemmin syötetty nimi")
  else:
    print("Uusi nimi")
    names.add(name)

for name in names:
  print(name)