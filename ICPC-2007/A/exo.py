import os

def bloodChild(bloodType1,bloodType2):
    res = "{"
    if(bloodType1 == "O+"):
        if(bloodType2 == "A+"):
            res += "A+, A-"
        if(bloodType2 == "B"):
            res += "A"
        if(bloodType2 == "O+"):
            res += "O+"
        if(bloodType2 == "O-"):
            res += "O+, O-"
    return res + "}"

def bloodParent(bloodType1,bloodType2):
    res = "{"
    return res + "}"

class Famille: 
    objets_crees = 0

    def __init__(self,tab): 
        Famille.objets_crees+=1
        self.parent1 = tab[0]
        self.parent2 = tab[1]
        self.child = tab[2]
        self.name = "Case "+str(Famille.objets_crees)

    def searchBloodType(self):
        if(self.parent1=='?'):
            self.parent1 = bloodParent(self.parent2,self.child)
        if(self.parent2=='?'):
            self.parent2 = bloodParent(self.parent1,self.child)
        if(self.child=='?'):
            self.child = bloodChild(self.parent1,self.parent2)

    def printBloodType(self):
        print(self.name+": "+self.parent1+" "+self.parent2+" "+self.child)


### Ouverture du fichier
working_directory = os.getcwd().replace("\\",'/')
file_path = working_directory + '/ICPC-2007/A/blood.in'
mon_fichier = open(file_path,"r")

ligne = mon_fichier.readline().split()
while(ligne):
    if(ligne[0]=='E' and ligne[1]=='N' and ligne[2]=='D'):
        break
    cas = Famille(ligne)
    cas.searchBloodType()
    cas.printBloodType()
    ligne = mon_fichier.readline().split()

### Fermeture du fichier
print()
mon_fichier.close()