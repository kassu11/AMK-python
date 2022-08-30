# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
# (Oikea käyttäjätunnus on python ja salasana rules).

yrityksia_jaljella = 5

while yrityksia_jaljella > 0:
  kayttaja = input("Kirjaudu sisään: ")
  salasana = input("Anna salasana: ")
  if kayttaja == "python" and salasana == "rules":
    print("Tervetuloa!")
    break
  else:
    yrityksia_jaljella -= 1
    print(f"Käyttäjätunnus tai salasana on väärin. Yritä uudelleen ({yrityksia_jaljella} yritystä jäljellä)")