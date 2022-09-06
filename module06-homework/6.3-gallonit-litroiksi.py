# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. 
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. 
# Muunnos on tehtävä aliohjelmaa hyödyntäen. 
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def gallonsToLiters(gallons):
  return gallons * 3.78541178

while True:
  gallons = float(input("Anna gallonamäärä: "))

  if gallons >= 0:
    print(f"{gallons} gallonaa on {gallonsToLiters(gallons):.2f} litraa")
  else:
    print("Lopetetaan toiminta.")
    break