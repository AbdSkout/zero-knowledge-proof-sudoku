class proof:
    def __init__(self):
        self.sodoku=[[5,4,3,8,9,7,6,2,1]
                     ,[8,1,6,2,4,5,9,3,7]
                     ,[9,2,7,3,6,1,4,5,8]
                     ,[1,6,5,4,8,2,7,9,3]
                     ,[3,9,8,7,5,6,1,4,2]
                     ,[2,7,4,9,1,3,5,8,6]
                     ,[4,3,2,6,7,9,8,1,5]
                     ,[6,5,9,1,3,8,2,7,4]
                     ,[7,8,1,5,2,4,3,6,9]]


    def column(self,n):
        lcolumn=list()
        for i in range(0,9):
            lcolumn.append(self.sodoku[i][n])
        print(lcolumn)
        return lcolumn

    def row(self,n):
         print(self.sodoku[n])
         return self.sodoku[n].copy()

    def Print(self):
        for i in range(0,9):
            
            for j in range(0,9):
                print(self.sodoku[i][j],end='')
                if (j!=0 and (j+1)%3==0):
                    print(" | ", end='' )
            print("")
            if(i!=0 and (i+1)%3==0):
                print(" - "*6)
                



