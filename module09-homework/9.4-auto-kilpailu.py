# Nyt ohjelmoidaan autokilpailu. 
# Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. 
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. 
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. 
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. 
# Sitten kilpailu alkaa. 
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
  # Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. 
  # Tämä tehdään kutsumalla kiihdytä-metodia.
  # Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. 
  # Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. 
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

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

autot = []

for i in range(10):
  rekkari = "ABC-" + str(i + 1)
  nopeus_raja = random.randint(100, 200)
  auto = Auto(rekkari, nopeus_raja)
  autot.append(auto)

matka_saavutettu = False
while not matka_saavutettu:
  for auto in autot:
    if auto.matka >= 10000: matka_saavutettu = True
    auto.kiihdyta(random.randint(-10, 15))
    auto.kulje(1)

print(f'{"Rekisteri numero":<20} {"Huippunopeus":<15} {"Nopeus":<10} {"Matka":<20}')
for auto in autot:
  max_nopeus = f"{auto.huippunopeus} km/h"
  nopeus = f"{auto.nopeus} km/h"
  matka = f"{auto.matka} km"
  print(f"{auto.rekisteritunnus:<20} {max_nopeus:<15} {nopeus:<10} {matka:<20}")