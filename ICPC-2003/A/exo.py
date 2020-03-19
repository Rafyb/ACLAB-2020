import os

class Iles:
    objets_crees = 0
    def __init__(self,content): 
        Iles.objets_crees+=1
        self.tab = content
        self.name = "City "+str(Iles.objets_crees)

    def nb_iles(self):
        nb = 0
        return nb

    def nb_ponts(self):
        length = 0
        nb = 0 
        return nb, length 

    def afficher(self):
        print(self.name)
        if(self.nb_ponts()[0] == 0 and  self.nb_iles() == 0 ):
            print("No bridges are needed.")
        pass



### Ouverture du fichier
working_directory = os.getcwd().replace("\\",'/')
file_path = working_directory + '/ICPC-2003/A/bridges.in'
mon_fichier = open(file_path,"r")

### Fermeture du fichier
mon_fichier.close()