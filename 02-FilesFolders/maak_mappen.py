import os
bestand = open("klasgenoten.txt", "r")


tekst_regel = bestand.readline()

while tekst_regel:
    os.mkdir(tekst_regel)
    print(tekst_regel)
    tekst_regel = bestand.readline()

