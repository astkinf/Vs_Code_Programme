name = input("Hallo, wie heißt du? ")
aktuellesJahr = int(input("Welches Jahr haben wir? "))
geburtsjahr = int(input("In welchem jahr bist du geboren? "))
print("Hattest du dieses Jahr schon Gebutstag? ")
jaOderNein = int(input("Für ja gebe 0, für nein gebe 1 ein: "))
if jaOderNein == 0:
    print(name + ", dann bist du jetzt " + str(aktuellesJahr - geburtsjahr) + " Jahre alt.")
else:
    print(name + ", dann bist du jetzt " + str(aktuellesJahr - geburtsjahr - 1) + " Jahre alt.")