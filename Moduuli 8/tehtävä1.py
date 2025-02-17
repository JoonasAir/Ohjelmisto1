import mysql.connector

def haeICAO(ICAOkoodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident ='{ICAOkoodi}'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print(f"Antamasi ICAO-koodi ({ICAOkoodi}) kuului lentokentälle:\n{rivi[0]} joka sijaitsee kunnassa: {rivi[1]}.")
    else:
        print(f"Syöttämäsi ICAO-koodia ({ICAOkoodi}) ei löydy!")
   


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

ICAOkoodi = input("Syötä ICAO-koodi: ").strip().upper() #Muutetaan syöte isoiksi kirjaimiksi
haeICAO(ICAOkoodi)
