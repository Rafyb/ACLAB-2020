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

	    
def initialiser_pcc(sommet, graph,L,P):
    L=[INF for i in range(graph.size)]
    P=[-1 for i in range(graph.size)]
    L[sommet] = 0.0
    return L,P

def trouver_min(graph,L):
    mini = INF
    sommet = -1
    for i in range(graph.size):
        if L[i] <mini:
            mini=L[i]
            sommet= i
    return sommet

def maj_distance(graph,s1,s2,L,P):
    if L[s2] > L[s1] + graph.matrice[s1][s2]:
        L[s2] = L[s1] + graph.matrice[s1][s2]
        P[s2] = graph.ordre[s1]
    return L,P
    
def dijkstra (graph,A,B):
    mes_longueurs=[]
    mes_predecesseurs=[]
    mes_longueurs,mes_predecesseurs = initialiser_pcc(A,graph,mes_longueurs,mes_predecesseurs)
    G =graph
    i = A
    while G.size != 2:
        i= trouver_min(graph,mes_longueurs)
        G.remove_sommet(i)
        for j in range(graph.size):
            mes_longueurs,mes_predecesseurs = maj_distance(graph,i,j, mes_longueurs,mes_predecesseurs)
    print(mes_longueurs)
    print(mes_predecesseurs)
    return mes_longueurs,mes_predecesseurs
    


def return_lot(graph,A,B):
    nbr = graph.size #taille du graphe
    
    #A1 = graph.position_node(A) #position node A
    #B1= graph.position_node(B) #position node B
    
    newGraph = graph #nouveau graphe que l'on va modifier tel que distance entre A et B =INF
    lenAB = newGraph.matrice[A][B]
    newGraph.matrice[A][B] = INF
    res,res_chemin= dijkstra(newGraph,A,B)
    return  res,res_chemin

def analiser_tout_voisins(graph,A):
    lots_A=[]
    for i in range(graph.size):
        if (graph.matrice[A][i]!=INF):
            lots_A.append(return_lot(graph,A,i))
    return lots_A
    

def analiser_la_figure(graph):
    lots_all=[]
    for i in range(graph.size):
        lots_all.append(analiser_tout_voisins(graph,i))
    return lots_all

def main():
    global Graph
    global geometrique
    
    geometrique =[]
    read_table(geometrique)
    
    nodes = add_nodes(geometrique[0],Graph)
    graph=Graph(len(nodes),nodes)      
    link_sommet(geometrique[0],graph)
    graph.rename_ordre()
    graph.print_matrice()
    mes_longueurs,mes_predecesseurs = dijkstra(graph,0,1)
main()
