# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi. niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa.


while True:
  tuumat = float(input("Anna tuumamäärä: "))

  if tuumat > 0:
    print(f"{tuumat} tuumaa on {tuumat * 2.54}cm")
  else:
    print("Lopetetaan toiminta.")
    break