#!/usr/bin/env python

import random

'''
print intro
vraag naam speler
print uitleg
herhaal
    print galg
    print een streepje voor elke letter
    vraag letter (invoer)
    als invoer woord is:a
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

while True:
    teller = 0
    geheime_woord2 = ""
    foute_letters = ""
    goede_letters = ""
    
    geheime_woord = ['goochelaar', 'aankijken', 'eten', 'geweldig', 'muziek', 'oase', '', 'tijger','quiz', 'picknick']
    geheime_woord2 = random.choice ( geheime_woord )
    woordlengte = len(geheime_woord2)
    lijnen = "_ " * woordlengte
    print(lijnen)
    print("")

    while True:
        keuze = input("Kies voor 'l' of 'w' om het geheime woord te raden ")
        if keuze == "l":
            letter_speler = input("Geef je letter op ")
            if letter_speler.isalpha() == True:
                if len(letter_speler) == 1:
                    if letter_speler in goede_letters:
                        print("Dit letter heb je al geraden.")
                    if letter_speler in foute_letters:
                        print("Dit letter heb je al geraden.")
                        letters()
                    if letter_speler in geheime_woord2:
                        teller = teller + 1
                    #for i in range(geheime_woord2):
                        goede_letters += letter_speler
                        letters()
                    if (letter_speler not in geheime_woord2) and (letter_speler not in foute_letters):                   
                        foute_letters += letter_speler
                        print(foute_letters)
                        print("fout")
                        aantal_fouten = aantal_fouten + 1
                        galg(aantal_fouten)
                else:
                    print("Geef 1 letter op.")
            elif letter_speler.isalpha() == False:
                print("kies een letter")
            else:
                print("kies een letter")
           
        elif keuze == "w":
           woord_speler = input("Geef je woord op ")
           if woord_speler == geheime_woord2:
               teller = teller + 1
               print("Goed zo! Je hebt het geheime woord geraden.")
               break
           else:
               print("fout")
               aantal_fouten = aantal_fouten + 1
               galg(aantal_fouten)
               
    
    print("Wil je nog een potje spelen?")
    nog_een_keer = input("'ja' of 'nee' ")
    if nog_een_keer == "ja":
        print("")
        aantal_fouten = 0
    if nog_een_keer == "nee":
        print("Tot de volgende keer.")
        print("Je hebt " + str(teller) + " punt(en) gehaald")
        break
    
    '''
    else:
        geheim()
        kies(teller)
'''


'''
geheim()
while True:
    kies(teller)
    if "nee" in galg:
        break
 '''     
print("het spel is afgelopen")    
