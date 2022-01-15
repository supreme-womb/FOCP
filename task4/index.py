import csv

class Team:
    def __init__(self,team):
        self.getteam(team)
        self.getP(0)
        self.getW(0)
        self.getD(0)
        self.getL(0)
        self.getF(0)
        self.getA(0)
        self.getDiff(0)
        self.getPts(0)

    def getteam(self,team):
        self.team=team

    def getP(self,P):
        self.P=P

    def getW(self,W):
        self.W=W

    def getD(self,D):
        self.D=D
    
    def getL(self,L):
        self.L=L

    def getF(self,F):
        self.F=F

    def getA(self,A):
        self.A=A

    def getDiff(self,Diff):
        self.Diff=Diff

    def getPts(self,Pts):
        self.Pts=Pts

    def setteam(self):
        return self.team

    def setP(self):
        return self.P

    def setW(self):
        return self.W

    def setD(self):
        return self.D

    def setL(self):
        return self.L

    def setF(self):
        return self.F

    def setA(self):
        return self.A

    def setDiff(self):
        return self.Diff

    def setPts(self):
        return self.Pts

    def getscore(self,F,A):
        self.getF(self.setF()+F)
        self.getA(self.setA()+A)
        self.getP(self.setP()+1)
        self.getDiff(self.setDiff()+(F-A)) 

        if F > A:
            self.getW(self.setW()+1)
            self.getPts(self.setPts()+3)

        elif F<A:
            self.getL(self.setL()+1)

        else:
            self.getD(self.setD()+1)
            self.getPts(self.setPts()+1)

def key(e):
    return e.setPts()
        
          
teams=[]
lst=[]
path1 = "/Users/susankafle/Desktop/untitled folder/task4/team.csv"
path2 = "/Users/susankafle/Desktop/untitled folder/task4/result.csv"
file=open(path1,"r")
for i in file:
    team =  Team(i.replace("\n",""))
    teams.append(team)
file = open(path2,"r")
for i in file:
    lst=i.replace("\n","").split(",")
    for j in teams:
        if j.setteam()==lst[0]:
            j.getscore(int(lst[1]),int(lst[3]))
        elif j.setteam()==lst[2]:
            j.getscore(int(lst[3]),int(lst[1]))

teams.sort(reverse=True, key=lambda e: (e.setPts(), e.setDiff()))
for i in teams:
    print(f"{i.setteam()},{i.setP()},{i.setW()},{i.setD()},{i.setL()},{i.setF()},{i.setA()},{i.setDiff()},{i.setPts()}")