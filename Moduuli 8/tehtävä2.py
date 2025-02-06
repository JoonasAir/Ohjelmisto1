#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. 
#Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
import mysql.connector


def maakoodiHaku(maakoodi):
    sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            type, maara = rivi #puretaan saatu rivi kahteen listaan
            print(type, maara)
    else:
        print("Ei tietoja")



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

maakoodi = input("Syötä maakoodi: ").strip().upper()
maakoodiHaku(maakoodi)
