#!/usr/bin/env python

import random

naam = input("Typ jouw naam ")
print ("Hallo " + naam + " welkom bij galgje")
##    break
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
        print("____")
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
        print("----------")
        print("|/       |")
        print("|        0")
        print("|        |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("-----")
    elif aantal_fouten == 4:
        print("----------")
        print("|/       |")
        print("|        0")
        print("|       /|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("------")      
    elif aantal_fouten == 5:
        print("----------")
        print("|/       |")
        print("|        0")
        print("|       /|\\")
        print("|       / \\")
        print("|")
        print("|")
        print("|")
        print("|")
        print("-------")
        
              

while True:
    galg(aantal_fouten)


    
    
