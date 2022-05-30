##############################
# Opdracht 5 Beslissen       #
##############################

# Opdracht 5a
# Je kunt aan een computer vragen of twee dingen hetzelfde zijn of niet, of groter of kleiner.
# Dit kan met == (gelijk), != (niet gelijk), > (groter), < kleiner
# De computer antwoord dan in het engels met True (waar) of False (niet waar)
# Als je naar de volgende regels kijkt, kun je dan bedenken of de computer waar of niet waar zegt?
# Oh, en ja, je leert meteen een nieuwe functie:
# je kunt van een string vragen of hij ergens mee begint, of eindigt!

getal = 2
#print (getal == 2) # Waar of Niet waar?
#print (getal == 3) # Waar of Niet waar?
#print (getal < 3)  # Waar of Niet waar?

string = "Hello world!"
#print (string.startswith("Hello"))       # Waar of Niet waar?
#print (string.endswith("asdfasdfasdf"))  # Waar of Niet waar?

# Opdracht 5b
# De code hieronder laat weten of een getal deelbaar is door twee.
# Dat gebeurt met het % teken. Dit krijg je meestal niet op school, maar voor programmeurs
# is het heel handig: het laat zien of er een rest-waarde is als je twee getallen deelt.
# dus 4 % 2 = 0, maar 5 % 2 = 1
# maar ook 9 % 3 = 0 en 11 % 3 = 2
# Kun je de code testen?
# Kun je het zo aanpassen zodat er wordt gekeken of een getal deelbaar is door 3?

#getal = input ("Geef een getal: ")
#rest = int (getal) % 2
#if rest == 0: print (getal, "is even.")
#else:         print (getal, "is oneven.")

# Opdracht 5c
# Kun je iets maken wat:
#   Eerst een woord aan de gebruiker vraagt
#   Als het woord met een C begint, dan print je "Het woord start met de C!"
#   En anders print je "Het woord start niet met de C..."
# Het kan op meerdere manieren, kun je twee manieren bedenken?



# Opdracht 5d
# Hieronder staat een lange zin, met heel veel letters. Ook staat er een tellertje op nul.
# Kun je daaronder iets maken met for en met if zodat het aantal keer de letter "e" geteld wordt?
# Hint: doe iets met bijvoorbeeld for letter in langezin en met teller = teller + 1

langezin = """Je mag hier zelf een lange zin intypen. Bedenk maar iets. 
Het mag zelfs op twee regels staan, want ik heb hier drie aanhalingstekens 
gebruikt, en dan weet Python dat hij door moet lezen tot er weer ergens 
drie aanhalingstekens staan"""
teller = 0


# Opdracht 5e
# Misschien voel je het al aankomen: Kun je nu de gebruiker een zin op laten geven,
# en daarna vragen welke letter hij wil tellen uit die zin? Print het antwoord op het scherm!
