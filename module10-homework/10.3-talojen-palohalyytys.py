# Jatka edellisen tehtävän ohjelmaa siten, 
# että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen. 
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.


class Hissi:
  def __init__(self, alin_kerros, ylin_kerros):
    self.alin_kerros = alin_kerros
    self.ylin_kerros = ylin_kerros
    self.kerros = alin_kerros

  def siirry_kerrokseen(self, kerros):
    if kerros >= self.alin_kerros and kerros <= self.ylin_kerros:
      while self.kerros < kerros:
        self.kerros_ylös()
      while self.kerros > kerros:
        self.kerros_alas()
    else: print("Kerrosta ei ole olemassa")
  
  def kerros_ylös(self):
    if(self.kerros < self.ylin_kerros):
      self.kerros += 1
      print(f"Kerroksessa {self.kerros}")

  def kerros_alas(self):
    if(self.kerros > self.alin_kerros):
      self.kerros -= 1
      print(f"Kerroksessa {self.kerros}")

class Talo:
  def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
    self.alin_kerros = alin_kerros
    self.ylin_kerros = ylin_kerros
    self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

  def aja_hissiä(self, hissi, kerros):
    if hissi <= len(self.hissit):
      print(f"[Hissi {hissi}] aktivoituu")
      self.hissit[hissi-1].siirry_kerrokseen(kerros)
    else: print("Hissiä ei ole olemassa")

  def palohälytys(self):
    for hissi in self.hissit:
      hissi.siirry_kerrokseen(self.alin_kerros)

t = Talo(1, 5, 3)
t.aja_hissiä(1, 3)
t.aja_hissiä(2, 5)
t.aja_hissiä(3, 4)
t.palohälytys()