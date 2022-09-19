# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. 
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, 
# että pieniä lentokenttiä on 65 kappaletta, 
# helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
  host="127.0.0.1",
  port= 3306,
  database="flight_game1",
  user="root",
  password="Salasana1",
  autocommit=True
)

def search_country_airport(iso_country):
  sql = f"""SELECT type FROM airport WHERE iso_country="{iso_country.upper()}";"""
  cursor = connection.cursor()
  cursor.execute(sql)
  return cursor.fetchall()

results = search_country_airport(input("Kirjoita maakoodi: "))
airpor_size_count = {}
for result in results:
  if result in airpor_size_count:
    airpor_size_count[result] += 1
  else:
    airpor_size_count[result] = 1

for key, value in airpor_size_count.items():
  print(f"""Lentokenttätyyppi: "{key[0]}" on {value} kpl.""")