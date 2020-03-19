import math as m

INF = 10000000000000.0

class Graph(object):
    def __init__(self,size, sommet =None):
        self.matrice =[]
        self.ordre = []
        self.size = size
        
        for i in range(size):
            self.matrice.append([])
            self.ordre.append(i)
            for j in range(size):
                self.matrice[i].append(INF)
        self.size = size
        if(sommet):
            self.initialisation_nom(sommet)

    #initialise les noms du tableau   
    def initialisation_nom(self,list_nom):
        if(len(list_nom)!=self.size):
            print("Erreur, la liste a trop/pas assez de nom")
            return 0
        else:
            for i in range(self.size):
                self.ordre[i] =list_nom[i]
                
    #Affiche la position de la node
    def position_node(self,node_name):
        return self.ordre.index(node_name)

    #node = entier 
    #return la liste des voisins et leur distances
    def voisin_dist(self,node):
        voisin = []
        return [ self.matrice[node][i] for i in range(self.size)]

    def nbr_voisins(self,node):
        j=0
        for i in range(self.size):
            if (self.matrice[node][i]!=INF):
                j+=1
        return j

    def remove_sommet(self,node):
        new_matrice=[]
        new_ordre=[]
        k=0
        i=0
        while (k<self.size-1):
            if(i!=node):
                new_matrice.append([])
                new_ordre.append(self.ordre[i])
                for j in range(self.size):
                    if(j!=node and k!=node):
                        new_matrice[k].append(self.matrice[k][j])
                k+=1
            i+=1
        new_matrice.pop(node)
        self.matrice = new_matrice
        self.ordre = new_ordre
        self.size -=1

    def rename_ordre(self):
        for i in range(self.size):
            self.ordre[i]=i
    #Affiche la matrice du graphe  
    def print_matrice(self):
        for i in range(len(self.matrice)):
            if(i==0):
                print("\t",end="")
                for y in range(len(self.matrice)):
                    print(self.ordre[y],end="\t")
            print()
            print(self.ordre[i],end="\t")
            for j in range(len(self.matrice)):
                if(self.matrice[i][j]==INF):
                    print("INF", end="\t")
                else:
                    print("%.2f" %self.matrice[i][j], end="\t")
        print()
                    
                
                


#permet de lire les entrée
def read_table(geometrique):
    fread = open("input.txt","r")
    segment_count = ""
    segments = []
    case = []
    segment = ""

    while(segment_count != 0):
        segment_count = fread.readline()
        segment_count = int(segment_count)
        for i in range(segment_count):
            segment = fread.readline()
            case = segment.split()
            case = list(map(int,case))
            segments.append(case)


        geometrique.append(segments)
        segments = []
    fread.close()
    return geometrique

# segment = un pointeur vers un segment
# point = 0 ou 1, permet de renvoyer les deux premiere valeur du segment sur 0, et les deux dernieres sur un
# return = une string qui identifie le point
def create_name_sommet(segment,point):
    point = point*2
    x= str(segment[point])
    y= str(segment[point+1])
    return x+y

# segment = pointeur vers un segment
# return = la distance entre le point A(segment[0],segment[1]) et le point B(segment[2],segment[3])
def calcul_weight(segment):
    return float(m.sqrt( m.pow( segment[0]-segment[2] , 2 )+m.pow( segment[1]-segment[3] , 2 )))

# matrice: pointeur vers la figure
# graph : pointeur vers le graphe
# return : la liste de node
def add_nodes(matrice,graph):
    liste_sommet=[]
    A=""
    B=""
    for i in range(len(matrice)):
        A = create_name_sommet(matrice[i],0)
        B = create_name_sommet(matrice[i],1)
        liste_sommet.append( A )
        liste_sommet.append( B )
        
    return list(dict.fromkeys(liste_sommet))

    
# matrice : la figure dont on doit relier les sommets
# graph : l'objet graph a modifier
# premet d'ajouter les liens entre les nodes dans graph
def link_sommet(matrice,graph):
    for i in range(len(matrice)):
        x = graph.position_node(create_name_sommet(matrice[i],0))
        y = graph.position_node(create_name_sommet(matrice[i],1))
        w = calcul_weight(matrice[i])
        graph.matrice[x][y]=w
        graph.matrice[y][x]=w


def testinf(chemin, restant):
    res= restant[0]
    mini = chemin[restant[0]]
    for i in restant :
        if chemin[i]<mini:
            mini = chemin[i]
            res=i
    return (res,mini)


def voisin (i,j,graph):
    if (graph[i][j]!=INF):
        return True
    return False


def dijkstra (graph,a):
    l = len (graph)
    chemin= [INF for i in range (l)]
    precedent=[-1 for i in range (l)]
    restant = [i for i in range (l)]
    chemin[a]=0
    
    while restant != []:
        mini,dist=testinf(chemin,restant)
        for i in restant :
            if voisin(mini,i,graph):
                if (dist+graph[mini][i]<chemin[i]):
                    chemin[i]=dist+graph[mini][i]
                    precedent[i]=mini
        restant.remove(mini)
        
    return chemin,precedent

def get_chemin(graph,a,b,chemin,precedent):
    longueur=chemin[b]
    chemin=[]
    i=precedent[b]
    chemin.append(b)
    while (i!=a and i!=-1):
        chemin.append(i)
        i=precedent[i]
    chemin.append(i)
    return longueur,chemin
    


def return_lot(graph,A,B):
    nbr = graph.size #taille du graphe
    
    #A1 = graph.position_node(A) #position node A
    #B1= graph.position_node(B) #position node B
    newGraph =None
    newGraph = graph #nouveau graphe que l'on va modifier tel que distance entre A et B =INF
    
    lenAB = newGraph.matrice[A][B]
    
    newGraph.matrice[A][B] = INF
    newGraph.matrice[B][A] = INF
    
    chemin,precedent = dijkstra(newGraph.matrice,A)
    res,res_chemin= get_chemin(newGraph,A,B,chemin,precedent)
    
   newGraph.matrice[A][B] = lenAB
    newGraph.matrice[B][A] = lenAB
    return  res,res_chemin   


def is_same(lot_A,lot_B):
    if len(lot_A)==len(lot_B):
        common=[]
        for x in lot_A:
            if x in lot_B:
                common.append(x)
        if len(common)==len(lot_B):
            return True
    return False

def enlever_doublons(lots):
    print("new")
    lots2= []
    i=0
    for i in range(len(lots)):
        lots2.append(set(lots[i][1]))
    i=0
    r =[]
    for i in range(len(lots2)):
        for j in range(i+1,len(lots2)):
            if is_same(lots2[i],lots2[j]):
                r.append(j)

    r= list(dict.fromkeys(r))
    for i in range(len(r)):
        del lots[len(r)-i]
    return lots
            
def analiser_tout_voisins(graph,A):
    lots_A=[]
    for i in range(graph.size):
        if (graph.matrice[A][i]!=INF):
            lots_A.append(return_lot(graph,A,i))
    return lots_A

def analiser_la_figure(graph):
    lots_all=[]
    for i in range(graph.size):
        lots_all=lots_all+(analiser_tout_voisins(graph,i))
    enlever_doublons(lots_all)
    return lots_all

def main():
    global graph
    global geometrique
    
    geometrique =[]
    read_table(geometrique)
    
    nodes = add_nodes(geometrique[0],Graph)
    graph=Graph(len(nodes),nodes)      
    link_sommet(geometrique[0],graph)
    graph.rename_ordre()

    
    
main()
