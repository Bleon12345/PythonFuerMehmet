# venv: virtual environment: hier werden die Bibliotheken (import...; z.B import random)
#abgespeichert mit einer bestimmten Version
# Das virtual environment wird durch eine 'requirements.txt' Datei abgebildet
#hiermit wird die Datei kreieiert:  pip3 freeze > requirements.txt

# < "kleiner als"
# größer als"
#for Schleifen
#Alle Zahlen zwischen 3 und 340 ausdrucken
"""for i in range(3, 341):
    print(i)

# Alle Zahlen zwischen -30 und 8000 (10er Schritte) ausdrucken

zaehler=-30
ende=8000
while zaehler<=ende:
    print(zaehler)
    zaehler = zaehler+10"""

# Alle Zahlen zwischen -160 und 75 inklusive (5er Schritte) ausdrucken

zaehler=-160
ende=75
while zaehler<=ende:
    print(zaehler)
    zaehler = zaehler+5


# Listen
# eine neue Liste mit mindestens 4 Elementen kreieren

liste = [4078.87, 1234.09, 7378.55, 3343.23]

#erste Element: Indexwert 0
#das erste element auf true setzen

liste[0] = True


#erste element: Indexwert 3
#das vierte element auf false setzen

liste[3] = False



#das dritte element auf hello world setzen
liste[2] = "Hello World"



# das erste element aus der liste entfernen

liste.remove(True)



liste.append("Hi Warudo")
print(liste)

# eine liste mit 2000 mal die 2 kreieren

list=[2]
print( 2000 * list)
list = 2000 * list
print(list)


