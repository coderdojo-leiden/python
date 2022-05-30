##############################
# Opdracht 3 Invoer          #
##############################

# Opdracht 3a
# Een functie is een taak die de computer uit moet voeren, en kun je herkennen aan de haakjes ()
# print() is ook zo'n taak: laat iets op het scherm zien.
# Een andere taak die de computer kan uitvoeren is om de gebruiker iets te vragen.
# Dit gebeurt ook met een functie: input("Dit stukje tekst komt op het scherm als vraag ").
# Kun jij eens aan de gebruiker vragen hoe oud hij is?
# Kun je dit ook printen op het scherm (zie bijvoorbeeld opdracht 2d)?



# Opdracht 3b
# Alles wat de gebruiker invoert is voor de computer een string. Dat wordt dus moeilijk rekenen.
# Een computer kan wel veel, maar niet uit zichzelf getallen omzetten naar tekst en omgekeerd.
# Willen we van de leeftijd weer een getal maken, dan hebben we weer een functie nodig: int()
# De functie int() maakt van hetgene tussen de haakjes weer een getal.
# Nu de opdracht net als 2c:
# Kun je nu de leeftijd vragen aan de gebruiker, en daarna printen hoe oud hij over 10 jaar is?
# Kun je ook printen hoe oud hij is als hij 2x zo oud is als nu?

#leeftijd = 
#print (leeftijd)  # Over tien jaar ben ik?
#print (leeftijd)  # hoe oud ben als ik twee keer zou oud ben als nu?

# Opdracht 3c
# Hierboven zouden we eigenlijk willen printen:
# print ("Over tien jaar ben je " + leeftijd + 10)
# Maar hier moeten we het getal weer omzetten naar tekst, dat kan de computer niet voor ons.
# Ook daar is gelukkig weer een functie voor: str()
# Deze taak maakt van hetgene tussen de haakjes een string.
# Kun je nu ook mooie zinnen maken met de leeftijden in opracht 3b?



# Opdracht 3d
# We weten nu wat een string is (touwtje tekst), een int (een heel getal), en een float (gebroken getal)
# En we hebben gezien hoe je operators kunt gebruiken (dus + - * /) om handelingen
# uit te voeren op types, maar dat dat alleen maar kan als alles van hetzelfde type is.
# Als laatste hebben we geleerd hoe je het ene type om kan zetten naar het andere.
# Kijk eens naar onderstaande regels. Kun je voorspellen wat er gaat gebeuren?
# controleer het door het 1 voor 1 uit te voeren, en verbeteren als dat nodig is.

getal = 13                     # we beginnen met een heel getal
#print (float (getal))              # Wat zou eruit komen als ik een int omzet naar float
#print ("Het getal is " + getal)    # Gaat dit goed? Hoe kun je dat verbeteren?
helft = getal / 2
#print (helft)                      # getal was een heel getal, maar is nu gebroken!
#print (int (helft))                # wat als je een gebroken getal weer heel maakt?
