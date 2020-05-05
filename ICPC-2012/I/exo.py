import os

class Verrou: 
    objets_crees = 0

    def __init__(self,r,c): 
        Verrou.objets_crees+=1
        row = []
        for i in range(0,r):
            col = []
            for j in range(0,c):
                col.append(0)
            row.append(col)
        self.syst = row
        self.name = "Cas "+str(Verrou.objets_crees)

    def insererMiroir(self,k,r,c):
        #print(str(r)+","+str(c))
        self.syst[r-1][c-1] = k

    def parcoursLaser(self):
        return False

    def parcoursInverse(self):
        pos = [-1,-1,-1]
        return pos

    def deverouillage(self):
        if(self.parcoursLaser()):
            print(self.name+': 0')
            return
        miroir = self.parcoursInverse()
        if(miroir[0] != -1):
            self.insererMiroir(miroir[0],miroir[1],miroir[2])
            if(self.parcoursLaser()):
                print(self.name+': '+str(miroir[0])+' '+str(miroir[1])+' '+str(miroir[2]))
                return
        print(self.name+': impossible')


### Ouverture du fichier
working_directory = os.getcwd().replace("\\",'/')
file_path = working_directory + '/ICPC-2012/I/config.in'
mon_fichier = open(file_path,"r")

ligne = mon_fichier.readline().split()
while(ligne):
    # Création du systeme
    ver = Verrou(int(ligne[0]),int(ligne[1]))
    # Insertion des miroirs de type /
    for mirroir1 in range(0,int(ligne[2])):
        mir = mon_fichier.readline().split()
        ver.insererMiroir(2,int(mir[0]),int(mir[1]))
    # Insertion des miroirs de type \
    for mirroir2 in range(0,int(ligne[3])):
        mir = mon_fichier.readline().split()
        ver.insererMiroir(1,int(mir[0]),int(mir[1]))
    # Resolution du systeme
    ver.deverouillage()
    # Next case     
    ligne = mon_fichier.readline().split()

### Fermeture du fichier
print()
mon_fichier.close()