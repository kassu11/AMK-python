# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). 
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. 
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

seasons = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

month_number = int(input("Kirjoita kuukausi numerona: "))
print("Vuoden aika on", seasons[month_number - 1])