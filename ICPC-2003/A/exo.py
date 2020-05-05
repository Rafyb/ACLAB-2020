import os

class Building:
    objets_crees = 0
    def __init__(self,x,y): 
        self.id = Building.objets_crees
        self.x = x
        self.y = y
        self.liee = []
        Building.objets_crees += 1

    def est_voisin(self,other):
        if( (self.x == other.x and (self.y == other.y+1 or self.y == other.y-1) ) or (self.y == other.y and (self.x == other.x+1 or self.x == other.x-1))):
            return True
        return False
    
    def setMarked(self,num):
        self.numile = num

    def getMarked(self,num):
        return self.numile

    def setPont(self, ile):
        self.liee.append(ile)
        ile.liee.append(self)

    def estLiee(self, ile, parent):
        if(ile in self.liee):
            return True
        else :
            for otherile in self.liee:
                if(otherile != parent):
                    if(otherile.estLiee(ile,self)):
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
                tab.append(self.distanceEntre(self.sommets[i],self.sommets[j]))
            self.graphe.append(tab)
    
    def distanceEntre(self,sommet1,sommet2):
        # 0 => il n'y a aucun lien possible entre ces 2 parties
        # -1 => les 2 parties sont adjacentes
        # >0 => la distance entre les 2
        distance = 0
        if(sommet1 == sommet2):
            return distance
        if(sommet1.est_voisin(sommet2)):
            distance = -1
        else :
            if(sommet1.y == sommet2.y or sommet1.y == sommet2.y+1 or sommet1.y == sommet2.y-1):
                if(sommet1.x > sommet2.x):
                    distance = abs(sommet1.x - sommet2.x -1)
                else :
                    distance = abs(sommet2.x - sommet1.x -1)
            elif(sommet1.x == sommet2.x or sommet1.x == sommet2.x+1 or sommet1.x == sommet2.x-1):
                if(sommet1.y > sommet2.y):
                    distance = abs(sommet1.y - sommet2.y -1)
                else :
                    distance = abs(sommet2.y - sommet1.y -1)
        return distance
  
    def parcours(self,currentS,pile,num):
        parcouru = []
        currentS.setMarked(num)
        for idx in range(0,len(pile)):
            if(pile[idx].est_voisin(currentS)):
                parcouru.append(pile[idx])
        for build in parcouru:
            pile.pop(pile.index(build))
            self.parcours(build,pile,num)
        pass

    def nb_iles(self):
        pile = self.sommets.copy()
        nb = 0
        while(len(pile)>0):
            currentS = pile.pop(0)
            self.parcours(currentS,pile,nb)
            nb+=1
        return nb

    def nb_ponts(self,nb_ile):
        length = 0
        nb = 0 
        for valmax in range(1,self.width):
            for col in range(0,len(self.graphe)):
                for row in range(0,len(self.graphe[0])):
                    if(self.graphe[col][row] == valmax):
                        if(self.sommets[col].estLiee(self.sommets[row],self.sommets[col])):
                            self.graphe[col][row] = 0
                        else:
                            self.sommets[col].setPont(self.sommets[row])
                            nb+=1
                            length+=valmax
        return nb, length 

    def afficherMatrice(self):
        for ligne in self.graphe:
            print(ligne)

    def afficher(self):
        print(self.name)
        # On calcul le nombre d'iles séparées
        nb_ile = self.nb_iles()
        nb_pont = 0
        # Si il y a plus d'une ile on calcul le nombre de pont utile
        if(nb_ile > 1):
            ponts = self.nb_ponts(nb_ile)
            nb_pont = ponts[0]
            length = ponts[1]
            if(nb_pont == 0 and nb_ile > 1):
                print("No bridges are possible.")
            else:
                print(str(nb_pont)+" bridges of total length "+str(length))
            if(nb_ile - nb_pont > 1):
                print(str(nb_ile - nb_pont)+" disconnected groups")
        else :
            print("No bridges are needed.")
        
        # Debug
        '''
        print("Matrice :")
        self.afficherMatrice()
        print("Nb d'ile : "+str(nb_ile)) 
        '''
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