from auto import Auto

class Sähköauto(Auto):
  def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
    super().__init__(rekisteritunnus, huippunopeus)
    self.akkukapasiteetti = akkukapasiteetti