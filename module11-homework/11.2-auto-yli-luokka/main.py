# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. 
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. 
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. 
# Kirjoita aliluokille alustajat. 
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. 
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. 
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). 
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

from sähköauto import Sähköauto
from polttomoottori import Polttomoottori

sähkö = Sähköauto("ABC-15", 180, 52.5)
poltto = Polttomoottori("ACD-123", 165, 32.3)

sähkö.kiihdyta(100)
poltto.kiihdyta(50)

sähkö.kulje(3)
poltto.kulje(3)

print("Sähköauto: ", sähkö.matka)
print("Polttomoottoriauto: ", poltto.matka)