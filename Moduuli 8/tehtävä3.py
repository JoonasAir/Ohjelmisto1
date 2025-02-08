import mysql.connector
from geopy import distance

def hae_koordinaatit(koordinaatit):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{koordinaatit}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos:
            return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1', #"localhost" käy myös
         port= 3306,
         database='flight_game',
         user='joonas',
         password='sqlpassu',
         charset="utf8mb4",
         collation="utf8mb4_unicode_ci",
         autocommit=True
         )

ICAOkoodi1 = input("Syötä ensimmäinen ICAO-koodi: ").strip().upper()
ICAOkoodi2 = input("Syötä toinen ICAO-koodi: ").strip().upper()

koord1 = hae_koordinaatit(ICAOkoodi1)
koord2 = hae_koordinaatit(ICAOkoodi2)

if not koord1 and not koord2:
      print(f"Kumpaakaan ICAO-koodia ei löytynyt tietokannasta! (Syötit koodit {ICAOkoodi1} ja {ICAOkoodi2})")
elif not koord1:
      print(f"Antamaasi {ICAOkoodi1} ICAO-koodia ei löytynyt tietokannasta!")
elif not koord2:
      print(f"Antamaasi {ICAOkoodi2} ICAO-koodia ei löytynyt tietokannasta!")
else:
    etaisyys_km = (distance.distance(koord1, koord2).km)
    print(f"Antamiesi ICAO-koodien perusteella lentokentät sijaitsevat toisistaan {etaisyys_km:.2f} kilometrin etäisyydellä.")