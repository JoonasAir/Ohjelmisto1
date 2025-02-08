import mysql.connector
from prettytable import PrettyTable #Käytetään prettytable kirjastoa tulostukseen taulukon muodossa

def maakoodiHaku(a):
    sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country = '{a}' GROUP BY type"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos: #Toistetaan koodilohko jos maakoodi löytyy
        taulukko = PrettyTable(["TYPE", "NUMBER"]) #Luodaan taulukko haetuille tiedoille otsikoilla Type ja Number
        for i in tulos:
            type, number = i #puretaan saatu tuple kahteen osaan
            taulukko.add_row([type, number]) #Lisätään taulukkoon riveittään muuttujat type ja number
            taulukko.add_divider() #Jaotellaan rivit viivalla
        print(taulukko)
    else:                      #Ajetaan tämä tuloste jos maakoodia ei löytynyt
        print(f"Ei löytynyt tulosta maakoodille {maakoodi}")

yhteys = mysql.connector.connect(
         host='127.0.0.1', #"localhost" käy myös
         port= 3306,
         database='flight_game',
         user='joonas',
         password='',
         charset="utf8mb4",
         collation="utf8mb4_unicode_ci",
         autocommit=True
         )

maakoodi = input("Syötä maakoodi: ").strip().upper()
maakoodiHaku(maakoodi)