data1=[]
names=[]
eMarks=[]
pMarks=[]
mMarks=[]
cMarks=[]
bMarks=[]
name1=""
eng1=""
maths1=""
physics1=""
chemistry1=""
bio1=""
line1=""
f1=open("marks.txt","r")
for i in range(0,26,1):   
    line1=f1.readline().strip()
    arr1=line1.split(",")
    name1=arr1[0]
    eng1=arr1[3]
    maths1=arr1[4]
    physics1=arr1[5]
    chemistry1=arr1[6]
    bio1=arr1[7]
    arr2=eng1.split(":")
    arr3=maths1.split(":")
    arr4=physics1.split(":")
    arr5=chemistry1.split(":")
    arr6=bio1.split(":")
    names.append(name1)  
    eMarks.append(int(arr2[1]))
    mMarks.append(int(arr3[1]))
    pMarks.append(arr4[1])
    cMarks.append(arr5[1])
    bMarks.append(arr6[1])
maxEmarks=max(eMarks)
maxMmarks=max(mMarks)
toppers_e=[]
toppers_m=[]
print(names)
print(eMarks)
print(mMarks)
#print(pMarks)
#print(cMarks)
#print(bMarks)
#print(maxEmarks)
print(maxMmarks)
for i in range(0,26,1):
    if eMarks[i]==maxEmarks:
        toppers_e.append(names[i])
    if mMarks[i]==maxMmarks:
        toppers_m.append(names[i])
print(toppers_e," are the toppers in english with marks",maxEmarks)
print(toppers_m," are the toppers in maths with marks",maxMmarks)   

