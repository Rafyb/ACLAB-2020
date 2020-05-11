import math as m

class TestDeFeu(object):
    def __init__(self,division,longueur,origine,second_point):
        self.longueur=longueur
        self.division=division
        self.origine=origine
        self.point_2=second_point
        self.vector=self.vector()

    def param(self):
        print("cube de taille n="+str(self.longueur))
        print("division d="+str(self.division))
        print("point d'origine"+str(self.origine))
        print("second point"+str(self.point_2))
        print("vecteur="+str(self.vector))

    def vector(self):
        vector=[]
        vector.append(self.point_2[0]-self.origine[0])
        vector.append(self.point_2[1]-self.origine[1])
        vector.append(self.point_2[2]-self.origine[2])
        return vector

    def trajectoire(self,lambdaa):
        x= self.origine[0]+(lambdaa*self.vector[0])
        y= self.origine[1]+(lambdaa*self.vector[1])
        z= self.origine[2]+(lambdaa*self.vector[2])
        return [x,y,z]

    def line(self):
        A = self.trajectoire(0)
        B = self.trajectoire(50)
        return [A,B]

    def equation_cartesienne(self):
        return(self.origine,self.vector)

#retourne les coordonnée du point sur le plan donnée, retourne 0 si la droite est parallèle ou appartient au plan, -1 si le plan n'est pas correct
#plan est un entier entre 0 et 2 (0=x;1=y,2=z)
def is_secante(objet_feu,plan,plan_coord):
    abc,xyz=objet_feu.equation_cartesienne()
    lambdaa = 0
    if(plan>=0 and plan<=2):
        if(xyz[plan] != 0):
##            print("droite est secante au plan et la coupe en un point")
            lambdaa = lambda_plane(abc,xyz,plan,plan_coord)
            return objet_feu.trajectoire(lambdaa)
        return 0
    return -1

#retourne le lambda tel que le point alpha appartiennent au plan donnée
#plan est un entier entre 0 et 2 (0=x;1=y,2=z)
def lambda_plane(abc,xyz,plan,plan_coord):
    if (plan>=0 and plan<=2):
        if(abc[plan]!=plan_coord):
            return (plan_coord-abc[plan])/xyz[plan]
        else:
            return 0
    return -1

#retourne un booléen determinant si le point donnée se trouve dans un cube
def point_in_cube(point,coor_min,coor_max):
    if (point[0] >= coor_min[0] and point[1] >= coor_min[1] and point[2] >= coor_min[2]):
        if (point[0] <= coor_max[0] and point[1] <= coor_max[1] and point[2] <= coor_max[2]):
            return True
    return False

def test_mini_cube(objet_feu,coor_min,coor_max):
    j=0 #0= face min, 1=face max
    k=0 #x,y,z
    table_point=[]
    while (k<3 and len(table_point)!=2):
        for j in range(2):
            if(j):
                new_point = is_secante(objet_feu,k,coor_min[k])
            else:
                new_point = is_secante(objet_feu,k,coor_max[k])
                
            if(new_point!=0 and new_point!=-1):
                if(point_in_cube(new_point,coor_min,coor_max)):
                    table_point.append(new_point)
        k+=1
    return table_point

#probleme se trouve la, lorsque l'on monte d'un étage
#retourne le volume d'eau perdu du mini_cube
def loss_water(objet_feu,coor_min,coor_max):
    length= objet_feu.longueur/objet_feu.division
    volume=pow(length,3)
    
    point_touche=test_mini_cube(objet_feu,coor_min,coor_max)
    mini=length
    if(point_touche):
        for i in range(len(point_touche)):
            if ((point_touche[i][2]-coor_min[2])<mini):
                mini=point_touche[i][2]-coor_min[2]
    
    return ((length-mini)/length)*volume

#permet de verifier combien d'eau totale tombe dans le récipient en bas
def tir_session(objet_feu):
    nombre_cube=objet_feu.division
    length= objet_feu.longueur/objet_feu.division
    eau_perdu=0
    for x in range(nombre_cube):
        for y in range(nombre_cube):
            for z in range(nombre_cube):
                eau_perdu += loss_water(objet_feu,[x*length,y*length,z*length],[(x+1)*length,(y+1)*length,(z+1)*length])
    return eau_perdu
    
def readFile():
    fread = open("bullet.in","r")
    segment = fread.readline()
    i=0
    while(segment!="0"):        
        segment = segment.split(" ")
        segment= list(map(int,segment))
        session.append(TestDeFeu(segment[0],segment[1],segment[2:5],segment[5:]))        
        i+=1
        segment = fread.readline()


def main():
    global session
    session = []
    readFile()
    session[0].param()
    print(session[0].line())
    print()
    for i in range (len(session)):
        print(tir_session(session[i]))
main()
