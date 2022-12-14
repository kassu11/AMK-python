# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. 
# Jokaisella julkaisulla on nimi. 
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. 
# Kirjoita luokkiin myös tarvittavat alustajat. 
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. 
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). 
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

from magazine import Magazine
from book import Book

lehti = Magazine("Aku Ankka", "Aki Hyyppä")
kirja = Book("Hytti n:o 6", 200, "Rosa Liksom")

lehti.print_info()
kirja.print_info()