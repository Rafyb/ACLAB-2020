import math as m

class TestDeFeu(object):
    def __init__(self,taille,volume,origine,second_point):
        self.taille=taille
        self.volume=volume
        self.origine=origine
        self.point_2=second_point
        self.line=self.trajectoire()

    def param(self):
        print("cube de taille n="+str(self.taille))
        print("Volume d="+str(self.volume))
        print("point d'origine"+str(self.origine))
        print("second point"+str(self.point_2))
        print("trajectoire="+str(self.line))

    def trajectoire(self):
        line=[]
        line.append([(self.origine[0]-self.point_2[0]),self.point_2[0]])
        line.append([(self.origine[1]-self.point_2[1]),self.point_2[1]])
        line.append([(self.origine[2]-self.point_2[2]),self.point_2[2]])
        return line

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
main()
