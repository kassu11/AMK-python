# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. 
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. 
# Uusi hissi on aina alimmassa kerroksessa. 
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. 
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. 
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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

h = Hissi(1, 5)
h.siirry_kerrokseen(3)
h.siirry_kerrokseen(1)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(100)
h.siirry_kerrokseen(1)