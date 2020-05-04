import os   
import re
motsLu = []

def regexMeta(string):
    return string.replace(',','').replace('\n','').replace('-','').replace('.','').replace("'",'')

def gestionMot(mot):
    number = re.findall(r'\d+', mot)
    if(number != []) :
        #print(number)
        mot = motsLu[len(motsLu)-int(number[0])]

    motreg = regexMeta(mot)
    if( motreg != ''):
        if(motreg in motsLu):
            motsLu.pop(motsLu.index(motreg))
        motsLu.append(motreg)
    return mot


def numberToWord(number):
    #print(number)
    return motsLu[len(motsLu)-int(number[0])]


def uncompress(fichier):
    texteLu = ''
    for mot in fichier.read().split(' '):
        # Gestion des carateres de séparation
        if(mot.find('-') != -1 or mot.find("'") != -1):
            if(mot.find("'") != -1) :
                motsDouble = mot.split("'")
                separation = "'"
            elif(mot.find('--') != -1):
                motsDouble = mot.split('--')
                separation = '--'
            else :
                motsDouble = mot.split('-')
                separation = '-'

            if(motsDouble[1] != ''):
                texteLu = texteLu + gestionMot(motsDouble[0]) + separation
                mot = motsDouble[1]
            else :
                texteLu = texteLu + gestionMot(motsDouble[0]) + separation
                mot = ''


        texteLu = texteLu +  gestionMot(mot) + " "
    return texteLu

### Ouverture du fichier
working_directory = os.getcwd().replace("\\",'/')
file_path = working_directory + '/ICPC-1995/H/uncomp.in'
mon_fichier = open(file_path,"r")

texteUncompressed = uncompress(mon_fichier)
print(texteUncompressed)

### Fermeture du fichier
mon_fichier.close()