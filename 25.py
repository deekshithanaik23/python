count=100
lucky=[]
unlucky=[]
prison=["C"]*count

for i in range(0,count,1):
    prison[i]="O"

for i in range(1,count,2):
    prison[i]="C"

for j in range(2,count,1):
    
    for i in range(j,count,j+1):
        if prison[i]=="C":
            prison[i]="O"
        else:
            prison[i]="C"
    
for i in range(0,count,1):    
    if prison[i]=="O":
        lucky.append(i+1)
    else:
        unlucky.append(i+1)
print("lucky prisoners",lucky,"will release today")
print("unlucky prisoners",unlucky,"will release after 4 weeks")
