from auto import Auto

class Polttomoottori(Auto):
  def __init__(self, rekisteritunnus, huippunopeus, tankki_koko):
    super().__init__(rekisteritunnus, huippunopeus)
    self.tankki_koko = tankki_koko