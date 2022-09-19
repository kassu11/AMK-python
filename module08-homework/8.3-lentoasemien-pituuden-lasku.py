# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. 
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. 
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin. 
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. 
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. 
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
  host="127.0.0.1",
  port= 3306,
  database="flight_game1",
  user="root",
  password="Salasana1",
  autocommit=True
)

def search_location(icao):
  sql = f"""SELECT latitude_deg, longitude_deg FROM airport WHERE ident="{icao.upper()}";"""
  cursor = connection.cursor()
  cursor.execute(sql)
  return cursor.fetchone()

a_location = search_location(input("Kirjoita lentoaseman ICAO-koodi: "))
b_location = search_location(input("Kirjoita lentoaseman ICAO-koodi: "))

distance_in_km = distance.distance(a_location, b_location).miles * 1.609344
print(f"""Lentoasemien välillä on {distance_in_km} km.""")