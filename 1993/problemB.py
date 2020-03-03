import networkx as nx
import math as m
geometrique = []

graphe =[]
#permet de lire les entrée
def read_table():
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
#initialise le graphe
def init_graph():
    return nx.Graph()

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
    return m.sqrt( m.pow( segment[0]-segment[2] , 2 )+m.pow( segment[1]-segment[3] , 2 ))

# matrice: pointeur vers la figure
# graph : pointeur vers le graphe
# rajoute les différentes nodes au graph
def add_nodes(matrice,graph):
    liste_sommet=[]
    A=""
    B=""
    for i in range(len(matrice)):
        A = create_name_sommet(matrice[i],0)
        B = create_name_sommet(matrice[i],1)
        liste_sommet.append( A )
        liste_sommet.append( B )
        
    graph.add_nodes_from(list(dict.fromkeys(liste_sommet)))

    
# matrice : la figure dont on doit relier les sommets
# graph : l'objet graph a modifier
# premet d'ajouter les liens entre les nodes dans graph
def link_sommet(matrice,graph):
    for i in range(len(matrice)):
        graph.add_edge( create_name_sommet(matrice[i],0) , create_name_sommet(matrice[i],1), weight = calcul_weight(matrice[i]))
        graph.add_edge( create_name_sommet(matrice[i],1) , create_name_sommet(matrice[i],0), weight = calcul_weight(matrice[i]))
        
def voisin(matrice, sommet):
    return list(matrice.neighbors(sommet))

def main():
    global Graph
    Graph =init_graph()
    read_table()
    link_sommet(geometrique[0],Graph)
    print(voisin(Graph,'1041'))

main()
