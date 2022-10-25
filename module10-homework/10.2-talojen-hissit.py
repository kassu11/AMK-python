# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. 
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. 
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. 
# Hissien lista tallennetaan talon ominaisuutena. 
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. 
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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

t = Talo(1, 5, 2)
t.aja_hissiä(1, 3)
t.aja_hissiä(2, 5)
t.aja_hissiä(2, 100)
t.aja_hissiä(2, 1)
t.aja_hissiä(10, 1)
t.aja_hissiä(1, 1)