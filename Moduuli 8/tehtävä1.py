#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen 
#ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. 
#ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.


import mysql.connector

def haeICAO(ICAOkoodi):
    sql = f"SELECT name FROM airports WHERE ident ='{ICAOkoodi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        print(f"Antamasi ICAO-koodi kuului lentokentälle {tulos}")


yhteys = mysql.connector.connect(
         host='127.0.0.1', #"localhost" käy myös
         port= 3306,
         database='airport',
         user='',
         password='',
         autocommit=True
         )

ICAOkoodi = input("Syötä ICAO-koodi: ").strip().upper() #Muutetaan syöte isoiksi kirjaimiksi
haeICAO(ICAOkoodi)