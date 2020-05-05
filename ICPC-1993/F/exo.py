import os

### Class Puzzle
class Puzzle: 
    objets_crees = 0

    def __init__(self,content): 
        Puzzle.objets_crees+=1
        self.tab = content
        self.name = "Puzzle #"+str(Puzzle.objets_crees)
        self.error = False

    def getPosVoid(self):
        for v in range(0,5) :
            for h in range(0,5) :
                if(self.tab[v][h] == ' '):
                    return (v,h)

    def up(self):
        v,h = self.getPosVoid()
        if(v==0) :
            self.error = True
            return False
        tmp = self.tab[v-1][h]
        self.tab[v-1][h] = self.tab[v][h]
        self.tab[v][h] = tmp
        return True

    def down(self):
        v,h = self.getPosVoid()
        if(v==4) :
            self.error = True
            return False
        tmp = self.tab[v+1][h]
        self.tab[v+1][h] = self.tab[v][h]
        self.tab[v][h] = tmp
        return True

    def left(self):
        v,h = self.getPosVoid()
        if(h==0) :
            self.error = True
            return False
        tmp = self.tab[v][h-1]
        self.tab[v][h-1] = self.tab[v][h]
        self.tab[v][h] = tmp
        return True

    def right(self):
        v,h = self.getPosVoid()
        if(h==4) :
            self.error = True
            return False
        tmp = self.tab[v][h+1]
        self.tab[v][h+1] = self.tab[v][h]
        self.tab[v][h] = tmp
        return True
    
    def executeSeq(self,seq):
        for action in seq :
            if(action=='A'):
                self.up()
            if(action=='B'):
                self.down()
            if(action=='L'):
                self.left()
            if(action=='R'):
                self.right()
        return True

    def afficher(self):
        print("\n"+self.name+":")
        if(self.error):
            print("  This puzzle has no final configuration.")
        else :
            for i in range(0,5) :
                print("  "+self.tab[i][0]+" "+self.tab[i][1]+" "+self.tab[i][2]+" "+self.tab[i][3]+" "+self.tab[i][4])
        pass

### Fonctions lecture de fichier
def readPuzzle(mon_fichier):
    tableau = []
    for i in range(0,5) :
        line = []
        for j in range(0,6) :
            c = mon_fichier.read(1)
            if(c=='Z') :
                return None
            if(c!='\n'):
                line.append(c)
        tableau.append(line)
    return tableau

def readSequence(mon_fichier):
    seq = []
    c = mon_fichier.read(1)
    while(c!='0'):
        if(c=='A' or 'B' or 'R' or 'L'):
            seq.append(c)
        c = mon_fichier.read(1)
    # Passer le \n
    mon_fichier.read(1)
    return seq

### Ouverture du fichier
working_directory = os.getcwd().replace("\\",'/')
file_path = working_directory + '/ICPC-1993/F/test.txt'
mon_fichier = open(file_path,"r")

### Lecture des puzzles
tabpuz = readPuzzle( mon_fichier )
while(tabpuz != None):
    puz = Puzzle( tabpuz )
    puz.executeSeq( readSequence( mon_fichier ))
    puz.afficher()
    tabpuz = readPuzzle( mon_fichier )

### Fermeture du fichier
print()
mon_fichier.close()

    