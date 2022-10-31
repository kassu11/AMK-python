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