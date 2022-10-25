# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. 
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. 
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. 
# Luokassa on seuraavat metodit:
  # tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
  # tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
  # kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". 
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. 
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa aja tunti-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. 
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random

class Auto:
  def __init__(self, rekisteritunnus, huippunopeus):
    self.rekisteritunnus = rekisteritunnus
    self.huippunopeus = huippunopeus
    self.nopeus = 0
    self.matka = 0

  def kiihdyta(self, maara):
    self.nopeus += maara
    if self.nopeus > self.huippunopeus:
      self.nopeus = self.huippunopeus
    elif self.nopeus < 0:
      self.nopeus = 0

  def kulje(self, tunnit):
    self.matka += round(self.nopeus * tunnit)

class Kilpailu:
  def __init__(self, nimi, pituus, auto_maara):
    self.nimi = nimi
    self.pituus = pituus
    self.autolista = []
    for i in range(auto_maara):
      rekkari = "ABC-" + str(i+1)
      nopeus_raja = random.randint(100, 200)
      self.autolista.append(Auto(rekkari, nopeus_raja))

  def tunti_kuluu(self):
    for auto in self.autolista:
      auto.kiihdyta(random.randint(-10, 15))
      auto.kulje(1)

  def tulosta_tilanne(self):
    print(f'{"Rekisteri numero":<20} {"Huippunopeus":<15} {"Nopeus":<10} {"Matka":<20}')
    for auto in self.autolista:
      max_nopeus = f"{auto.huippunopeus} km/h"
      nopeus = f"{auto.nopeus} km/h"
      matka = f"{auto.matka} km"
      print(f"{auto.rekisteritunnus:<20} {max_nopeus:<15} {nopeus:<10} {matka:<20}")

  def kilpailu_ohi(self):
    for auto in self.autolista:
      if auto.matka >= self.pituus:
        return True
    return False

kisa = Kilpailu("Suuri romuralli", 8000, 10)

while not kisa.kilpailu_ohi():
  kisa.tunti_kuluu()
kisa.tulosta_tilanne()