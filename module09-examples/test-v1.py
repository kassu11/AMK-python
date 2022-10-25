class Koira:
  jalka_maara = 4
  tehty = 0
  def __init__(self, nimi, syntymavuosi, rotu, paino, haukahdus = "hau"):
    self.nimi = nimi
    self.syntymavuosi = syntymavuosi
    self.rotu = rotu
    self.paino = paino
    self.haukahdus = haukahdus

    Koira.tehty += 1

  def hauku(self, kerrat):
    for i in range(kerrat):
      print(self.haukahdus)

koira1 = Koira("Musti", 2010, "Saksanpaimenkoira", 5, "nice")
koira2 = Koira("Ville", 2012, "Kultainen noutaja", 4)

print("koiran nimi on " + koira1.nimi + " ja sen rotu on " + koira1.rotu)
print("koiran nimi on " + koira2.nimi + " ja sen rotu on " + koira2.rotu)

koira1.hauku(3)
koira2.hauku(2)

koira1.jalka_maara = 2
print(koira2.jalka_maara)
Koira.jalka_maara = 3
print(koira2.jalka_maara)
print(">", koira1.jalka_maara)


print(koira1.tehty)
print(koira2.tehty)

lista = [i for i in range(10)]
print(lista)