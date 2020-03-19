#un arbre non-binaire permettant de simuler un arbre généalogique
# def __init__
# string name = nom de la personne
# Tree parent = de base null, sinon le paren
              
class Tree(object):            
    def __init__(self, name,parent=None,relation=None):
        self.child = []
        self.name = name

        if(parent):
            if(relation == 1 or not relation):
                define_children(parent,self,1)
            else:
                define_children(parent,self,relation)
    
def define_children(elder,younger,distance):
            if(distance==1):
                elder.child.append(younger)
            else:
                Tree("",elder)        
                define_children(elder.child[len(elder.child)-1],younger,distance-1)


def print_child(elder):
    if(elder.name !=""):
        print(elder.name,end='')
    else:
        print("P-Anon",end='')
    for i in range(len(elder.child)):
        if(i==0):
            print("(",end="")
            
        if(elder.child[i].name !=""):
            print(elder.child[i].name,end="")
        else:
            print("C-Anon",end="")
        
        if(i!=len(elder.child)-1):
            print(",",end="")
        else:
            print(")")
        

def print_tree(tree,relation):
    for i in range(relation):
        print("\t",end="")
    print_child(tree)
    if(tree.child):
        for i in range(len(tree.child)):
            print_tree(tree.child[i],relation+1)
            print("")
        

def comprehend_line(lines):
    final = lines[1:].split( )
    final = final[:3]
    final[2] = int(final[2])
    return final

def return_descendant(A,B):
    
    
def read_tree():
    fread = open("input.txt","r")
    lines=""
    content=""
    tree=[]
    while(content!="E"):
        lines=fread.readline()
        content=lines[:1]
        if(content=="R"):
            print("R")
        elif(content=="F"):
            print("F")
        elif(content=="#"):
            print("#")

        
Don= Tree("Don")
Mary = Tree("Mary",Don)
Peg = Tree("Peg",Mary,2)
Jean = Tree("Jean",Don)
John = Tree("John",Jean)
Stan = Tree("Stan",Jean)
Phil = Tree("Phil",Jean,3)

Sue = Tree("Sue")
define_children(Sue,Jean,1)

print_tree(Don,0)
print_tree(Sue,0)
read_tree()

