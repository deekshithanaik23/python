import random
import sys
f1=open("dictionary.txt","r")
list1=f1.readlines()
list2=[]
temp1=[]
userchoice1=""
compchoice1=""
userlastchar=""
complastchar=""
len1=len(list1)
for i in range(0,len1,1):    
    s1=list1[i].strip()
    list2.append(s1)

for i in range(0,10,1):
    if i==0:
        compchoice1=random.choice(list2)
        print("Computer:",compchoice1,end=", ")
    else:
        temp1=list(filter(lambda i:i.startswith(userlastchar),list2))
        compchoice1=random.choice(temp1)
        print("Computer:",compchoice1,end=", ")

    complastchar=compchoice1[-1]
    temp1=list(filter(lambda i:i.startswith(complastchar),list2))
    userchoice1=input("User:")
    userlastchar=userchoice1[-1]

    if userchoice1 in temp1:
        pass
    else:
        print("Lost")
        sys.exit()
    

