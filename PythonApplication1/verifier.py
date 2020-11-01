from random import seed
from random import randint
import time
class verifier:
    
    def __init__(self):
        self.sodoku=[[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1]]

        self.c=[0,1,2,3,4,5,6,7,8]
        self.r=[0,1,2,3,4,5,6,7,8]
        

    def check(self, test):
        l=test.copy()
        l.sort();
        for i in range(0,8):
            if l[i]!=-1:
                if l[i] == l[i+1] or  not(l[i]>=0 and l[i] <=9 and l[i+1]>=0 and l[i]<=9) :
                    return 0

        return 1        

    def get_row(self,row,n):
        self.check(row)
        for i in range(0,9):
            if self.sodoku[n][i]==-1:
                self.sodoku[n][i]=row[i]
            if self.sodoku[n][i]!=-1:
                if self.sodoku[n][i]!=row[i]:
                    return 0
        return self.check_smallbox()
    
    def get_cloumn(self,cloumn,n):
        self.check(cloumn)
        for i in range(0,9):
            if self.sodoku[i][n]==-1:
                self.sodoku[i][n]=cloumn[i]
            if self.sodoku[i][n]!=-1:
                if self.sodoku[i][n]!=cloumn[i]:
                    return 0
        return self.check_smallbox()
        


    def check_smallbox(self):
        l=[[],[],[],[],[],[],[],[],[]]
        for i in range(0,9):
            if  i>=0 and i<=2:
                index=0
            if i>=3 and i<=5:
                index=3
            if i>=6 and i<=8:
                index=6

            for j in range(0,9):
                if  0<=j and j<=2 :
                    l[index].append(self.sodoku[i][j])
                if 3<=j and j<=5 :
                     l[index+1].append(self.sodoku[i][j])
                if 6<=j and j<=8 :
                    l[index+2].append(self.sodoku[i][j])


        for i in range(0,9):
            
            if self.check(l[i]) ==0 :
                return 0

        return 1

    def ask(self):
        val=randint(0,8)
        R_C=randint(0,1)
        if len(self.c) ==0:
            R_C=0
        if len(self.r)==0:
            R_C=1
        if len(self.c)==0 and len(self.r)==0:
            return -1
        F=True
        if R_C ==1:
            while(F):
                if val in self.c:
                    F=False
                    self.c.remove(val)
                    print ("please give me column nubmber " , val+1)
                    time.sleep(0.5)
                    return [1,val]
                else:
                    val=randint(0,8)

             

        else:
            while(F):
                if val in self.r:
                    F=False
                    self.r.remove(val)
                    print( "please give me row nubmber" , val+1)
                    time.sleep(0.5)
                    return [0,val]
                else:
                    val=randint(0,8)

            

