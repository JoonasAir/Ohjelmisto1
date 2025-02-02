ICAOkoodit = {"EFAH": "Ahmosuon lentoasema, Oulu",
              "EFET": "Enontekiön lentoasema, Enontekiö",
              "EFIT": "Kiteen lentoasema, Kitee",
              "EFKU": "Kuopion lentoasema, Kuopio",
              "EFRY": "Räyskälän lentoasema, Loppi"}

valinta = int(input("Valitse toiminto syöttämällä numero (1-3)\n(1)Syötä uusi lentoasema\n(2)Hae lentoasemaa\n(3)Lopeta ohjelma\nSyötä numero: "))

while valinta != 3:
    if valinta == 1:
        uusiICAO = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()
        uusiNimi = input("Syötä lentoaseman nimi: ")
        ICAOkoodit[uusiICAO] = uusiNimi
        valinta = int(input("Valitse toiminto syöttämällä numero (1-3)\n(1)Syötä uusi lentoasema\n(2)Hae lentoasemaa\n(3)Lopeta ohjelma\nSyötä numero: "))
    elif valinta == 2:
        haku = input("Syötä lentoaseman ICAO koodi: ").strip().upper()
        if haku in ICAOkoodit:
            print(ICAOkoodit[haku])
        else:
            print("Lentoasemaa ei löytynyt!")
        valinta = int(input("Valitse toiminto syöttämällä numero (1-3)\n(1)Syötä uusi lentoasema\n(2)Hae lentoasemaa\n(3)Lopeta ohjelma\nSyötä numero: "))
    else:
        break

print("Ohjelma lopetetaan")
