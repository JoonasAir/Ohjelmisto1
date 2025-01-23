kayttaja = "python"
salasana = "rules"
kayttaja1 = ""
salasana1 = ""

kerrat = 0


while kerrat < 5 and kayttaja1 != kayttaja and salasana1 != salasana:
    kayttaja1 = input("Syötä käyttäjätunnus: ")
    salasana1 = input("Syötä salasana: ")
    if kayttaja1 == kayttaja and salasana1 == salasana:
        print("Tervetuloa!")
    else:
        print("Pääsy kielletty!")
    kerrat = kerrat +1