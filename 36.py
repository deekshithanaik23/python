import random
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

randnum=random.randint(0,len1-1)
compchoice1=list2[randnum]
print("Computer:",compchoice1)
userchoice1=input("User:")
len1=len(userchoice1)
userlastchar=userchoice1[len1-1:len1]
temp1=list(filter(lambda i:i.startswith(userlastchar),list2))
len1=len(temp1)
randnum=random.randint(0,len1-1)
compchoice1=temp1[randnum]
print("Computer:",compchoice1)
