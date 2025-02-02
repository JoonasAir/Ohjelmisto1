ICAOkoodit = {"EFAH": "Ahmosuon lentoasema, Oulu",
              "EFET": "Enontekiön lentoasema, Enontekiö",
              "EFIT": "Kiteen lentoasema, Kitee",
              "EFKU": "Kuopion lentoasema, Kuopio",
              "EFRY": "Räyskälän lentoasema, Loppi"}



while True:
    valinta = (input("Valitse toiminto syöttämällä numero (1-3)\n"
                        "(1)Syötä uusi lentoasema\n"
                        "(2)Hae lentoasemaa\n"
                        "(3)Lopeta ohjelma\n"
                        "Syötä numero: "))
    
    #Jos käyttäjä syöttää merkkijonon, ohjelma tulostaa siitä huomautuksen ja jatkaa while loopin alusta.
    if not valinta.isdigit():
        print("Syötä numero!")
        continue

    #Muutetaan syötä kokonaisluvuksi 
    valinta = int(valinta)


    if valinta == 1:
        uusiICAO = input("Syötä lentoaseman ICAO-koodi: ").strip().upper() #Muutetaan käyttäjän syöttämä merkkijono isoiksi kirjaimiksi
        uusiNimi = input("Syötä lentoaseman nimi: ")
        ICAOkoodit[uusiICAO] = uusiNimi
    elif valinta == 2:
        haku = input("Syötä lentoaseman ICAO koodi: ").strip().upper() #Muutetaan käyttäjän syöttämä merkkijono isoiksi kirjaimiksi
        if haku in ICAOkoodit:
            print(ICAOkoodit[haku])
        else:
            print("Lentoasemaa ei löytynyt!")
    elif valinta == 3:
        print("Ohjelma lopetetaan")
        break
    else:
        print("Väärä syöte, kokeile uudestaan!") #Jos käyttäjä syöttää jonkun muun luvun 1-3 ulkopuolelta, ohjelma pyytää syöttämään uuden luvun

    



