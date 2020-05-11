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

    def refleterLaser(self,miroir):
        if(miroir == 1) :
            if(self.direction == 'E') :
                self.direction = 'S'
            elif(self.direction == 'S') :
                self.direction = 'E'
            elif(self.direction == 'N') :
                self.direction = 'O'
            elif(self.direction == 'O') :
                self.direction = 'N'
        elif(miroir == 2) :
            if(self.direction == 'N') :
                self.direction = 'E'
            elif(self.direction == 'E') :
                self.direction = 'N'
            elif(self.direction == 'S') :
                self.direction = 'O'
            elif(self.direction == 'O') :
                self.direction = 'S'

    def affichage(self):
        ret = ''
        for x in range(0,len(self.syst)):
            for y in range(0,len(self.syst[0])):
                if(self.syst[x][y] == 1):
                    ret += '[\\]'
                elif(self.syst[x][y] == 2):
                    ret += '[/]'
                elif(self.syst[x][y] == 10):
                    ret += '[x]'
                elif(self.syst[x][y] == 11):
                    ret += '[o]'
                else :
                    ret += '[ ]'
            ret += '\n'
        print(ret)

    def parcoursLaser(self):
        self.direction = 'E'
        y = -1
        x = 0
        while(True):
            #Deplacement du laser
            if(self.direction == 'E') :
                y += 1
            if(self.direction == 'O') :
                y -= 1
            if(self.direction == 'S') :
                x += 1
            if(self.direction == 'N') :
                x -= 1
            #Condition d'arret
            if(x == len(self.syst) or x < 0 or y == len(self.syst[0]) or y < 0) :
                if(x == len(self.syst[0])-1 and y == len(self.syst) ):
                    return True
                else :
                    return False
            #Marquage de la case ou changement de direction
            if(self.syst[x][y] == 1 or self.syst[x][y] == 2) :
                self.refleterLaser(self.syst[x][y])
            else :
                self.syst[x][y] = 10
        return False

    def parcoursInverse(self):
        pos = [-1,-1,-1]
        self.direction = 'O'
        y = len(self.syst[0])
        x = len(self.syst)-1
        while(True):
            #Deplacement du laser
            if(self.direction == 'E') :
                y += 1
            if(self.direction == 'O') :
                y -= 1
            if(self.direction == 'S') :
                x += 1
            if(self.direction == 'N') :
                x -= 1
            #Condition d'arret
            if(x == len(self.syst) or x < 0 or y == len(self.syst[0]) or y < 0) :
                pos[1] += 1
                pos[2] += 1
                return pos
            #Assignement lors ce qu'on rencontre le laser
            if(self.syst[x][y] == 10):
                if(self.direction == 'N' or self.direction == 'O'):
                    pos = [1,x,y]
                if(self.direction == 'S' or self.direction == 'E'):
                    pos = [2,x,y]
            #Changement de direction
            elif(self.syst[x][y] == 1 or self.syst[x][y] == 2) :
                self.refleterLaser(self.syst[x][y])
            else :
                self.syst[x][y] = 11
        return pos

    def deverouillage(self):
        if(self.parcoursLaser()):
            print(self.name+': 0')
            return
        miroir = self.parcoursInverse()
        if(miroir[0] != -1):
            self.insererMiroir(miroir[0],miroir[2],miroir[1])
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