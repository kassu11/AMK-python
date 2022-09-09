# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. 
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. 
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. 
# (ICAO-koodi on lentoaseman yksilöivä tunniste. 
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. 
# Löydät koodeja helposti selaimen avulla.)

air_ports = {
  "EFET":	"Enontekiön lentoasema",
  "EFHK":	"Helsinki-Vantaan lentoasema",
  "EFIV":	"Ivalon lentoasema",
  "EFJO":	"Joensuun lentoasema",
  "EFKI":	"Kajaanin lentoasema",
  "EFKE":	"Kemi-Tornion lentoasema",
  "EFKT":	"Kittilän lentoasema",
  "EFKK":	"Kokkola-Pietarsaaren lentoasema",
  "EFKS":	"Kuusamon lentoasema",
  "EFLP":	"Lappeenrannan lentoasema",
  "EFMA":	"Maarianhaminan lentoasema",
  "EFMI":	"Mikkelin lentoasema",
  "EFOU":	"Oulun lentoasema",
  "EFPO":	"Porin lentoasema",
  "EFSA":	"Savonlinnan lentoasema",
  "EFSI":	"Seinäjoen lentoasema",
  "EFTU":	"Turun lentoasema",
  "EFVA":	"Vaasan lentoasema"
}

while True:
  print("#" * 50)
  print("1). Hae lintokenttä ICAO-koodilla")
  print("2). Lisää lentoasema")
  print("3). Lopeta")
  user_input = int(input("Kirjoita numero: "))

  if user_input == 1:
    icao = input("Kirjoita ICAO-koodi: ").upper()
    if icao in air_ports:
      print("\n" * 5 + air_ports[icao])
    else: print("\n" * 5 + "Lentoasemaa ei löytynyt")
  elif user_input == 2:
    icao = input("Kirjoita ICAO-koodi: ").upper()
    name = input("Kirjoita nimi: ")
    if icao in air_ports:
      print("\n" * 5 + "Lentoasema on jo olemassa")
    else:
      air_ports[icao] = name
      print("\n" * 5 + "Lentoasema lisätty")
  elif user_input == 3:
    break