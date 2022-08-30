# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

listOfNumbers = []

while True:
  userInput = input("Kirjoita luku tai tyhjä merkkijono lopettaaksesi: ")
  if userInput == "": break

  listOfNumbers.append(int(userInput))

listOfNumbers.sort(reverse=True)

print(f"Lista 5:tä suurimmasta numerostasi: {listOfNumbers[:5]}")