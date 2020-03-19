import os

class Building:
    objets_crees = 0
    def __init__(self,x,y): 
        self.id = Building.objets_crees
        self.x = x
        self.y = y
        Building.objets_crees += 1

    def est_voisin(self,other):
        if( (self.x == other.x and (self.y == other.y+1 or self.y == other.y-1) ) or (self.y == other.y and (self.x == other.x+1 or self.x == other.x-1))):
            return True
        return False

class City:
    objets_crees = 0
    def __init__(self,height,width): 
        City.objets_crees+=1
        self.name = "City "+str(City.objets_crees)
        self.height = height
        self.width = width

    def initialiser(self,fichier):
        ## Initialiser les sommets
        self.sommets = []
        nbblock = 0
        for h in range(0,self.height):
            for w in range(0,self.width+1):
                c = fichier.read(1)
                if(c=='#'):
                    self.sommets.append(Building(h,w))
                    nbblock += 1
        ## Initialiser le graphe
        self.graphe = []
        for i in range(0,nbblock):
            tab = []
            for j in range(0,nbblock):
                tab.append(0)
            self.graphe.append(tab)
        ## Ajout des arcs
        # 0 => il n'y a aucun lien entre ces 2 parties
        # -1 => les 2 parties sont adjacentes
        # >0 => la longueur du pont entre les 2 parties 
        parcoursS = self.sommets.copy()
        idxG = 0
        currentP = parcoursS.pop(0)
        while(len(parcoursS) > 0):
            for i in range(0,len(parcoursS)):
                if(currentP.est_voisin(parcoursS[i])):
                    self.graphe[idxG+(i+1)][idxG] = -1
            # On passe au sommet suivant
            currentP = parcoursS.pop(0)
            idxG+=1
  
    def parcours(self,pile,parcouru):
        currentS = pile.pop(0)
        parcouru.append(currentS)
        for idx in range(0,len(pile)):
            if(pile[idx].est_voisin(currentS)):
                parcouru.append(pile[idx])
        
        pass

    def nb_iles(self):
        pile = self.sommets.copy()
        parcouru = []
        nb = 0
        while(len(pile)>0):
            self.parcours(pile,parcouru)
            nb+=1

        return nb

    def nb_ponts(self):
        length = 0
        nb = 0 
        return nb, length 

    def afficherMatrice(self):
        for ligne in self.graphe:
            print(ligne)

    def afficher(self):
        nb_ile = self.nb_iles()
        nb_pont = self.nb_ponts()[0]
        print(self.name)
        print("Matrice :")
        self.afficherMatrice()
        
        if( nb_pont == 0 and  nb_ile == 0 ):
            print("No bridges are needed.")
        print()
        pass



### Ouverture du fichier
working_directory = os.getcwd().replace("\\",'/')
file_path = working_directory + '/ICPC-2003/A/bridges.in'
mon_fichier = open(file_path,"r")

ligne = mon_fichier.readline().replace('\n','').split(" ")
height = int(ligne[0])
width = int(ligne[1])

print()
while( width > 0 and width < 50 and height > 0 and width < 50):
    ville = City(height,width)
    ville.initialiser(mon_fichier)
    ville.afficher()
    ligne = mon_fichier.readline().replace('\n','').split(" ")
    height = int(ligne[0])
    width = int(ligne[1])

### Fermeture du fichier
mon_fichier.close()