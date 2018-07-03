'''
print intro
vraag naam speler
print uitleg
herhaal
    print galg
    print een streepje voor elke letter
    vraag letter (invoer)
    als invoer woord is:
        als woord is niet goed
            aantalfouten plus 1
        als woord wel goed
            woord is goed geef print gefeliciteerd + naam
            break
    anders
        als het meer letters zijn geef error
            break
        is letter een cijfer geef error
            break
        letter komt niet voor in woord zet een lijn bij galg erbij
            aantalfouten plus 1
        letter is goed
            vervang streepje door goede letter

puntentelling
vraag of degene nog een potje wil spelen
typ stop, het spel stopt
print bedankt voor het spelen
'''
import random

naam = input("Typ jouw naam ")
print ("Hallo " + naam + " welkom bij galgje")

aantal_fouten = 0

def galg(aantal_fouten):
    if aantal_fouten == 1:
        print("__________")
        print("|/       |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_____")
    elif aantal_fouten == 2:
        print("__________")
        print("|/       |")
        print("|        0")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_____")
    elif aantal_fouten == 3:
        print("__________")
        print("|/       |")
        print("|        0")
        print("|        |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_____")
    elif aantal_fouten == 4:
        print("__________")
        print("|/       |")
        print("|        0")
        print("|       /|\\")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_____")
    else:
        print("__________")
        print("|/       |")
        print("|        0")
        print("|       /|\\")
        print("|       / \\")
        print("|")
        print("|")
        print("|")
        print("|")
        print("_____")
        print("Het spel is afgelopen. Het goede woord was: " + geheime_woord2 + ". Wil je nog een potje spelen?")

'''
def nog_een_potje():
    nog_een_keer = input("'ja' of 'nee' ")
    if nog_een_keer == "ja":
#        kies(teller)
        if nog_een_keer == "nee":
            print("Tot de volgende keer.")
            print("Je hebt " + str(teller) + " punt(en) gehaald")
            break
'''

def letters():
    resultaat = ""
    for letter_speler in geheime_woord2:
        if letter_speler in goede_letters:
            resultaat += letter_speler
        else:
            resultaat += "_ "
    print(resultaat)


