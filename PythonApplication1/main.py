from proof import *
from verifier import *
p=proof()
v=verifier()

flag=1


while(flag):
    val=v.ask()
    if(val!=-1):
        l=[]
        if val[0]==1:
            l=p.column(val[1])
            flag=v.get_cloumn(l,val[1])
            if flag==0 :
                print("there are mistake in the sodoku")
        if val[0]==0:
            l=p.row(val[1])
            flag=v.get_row(l,val[1])
            if flag==0 :
                print("there are mistake in the sodoku")
    else:
        print("the sdoku is corect")
        flag=0



