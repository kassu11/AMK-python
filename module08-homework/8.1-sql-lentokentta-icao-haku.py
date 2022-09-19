# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.

import mysql.connector

connection = mysql.connector.connect(
  host="127.0.0.1",
  port= 3306,
  database="flight_game1",
  user="root",
  password="Salasana1",
  autocommit=True
)

def search_icao(icao):
  sql = f"""SELECT name, municipality FROM airport WHERE ident="{icao.upper()}";"""
  cursor = connection.cursor()
  cursor.execute(sql)
  return cursor.fetchall()

results = search_icao(input("Kirjoita lentoaseman ICAO-koodi: "))

for result in results:
  print(f"""Nimi: "{result[0]}" sijaitsee kunnassa: "{result[1]}".""")