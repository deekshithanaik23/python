f1=open("in3.txt","r")
f2=open("out3.txt","w")
s1=f1.readline().replace("\n","")
list1=s1.split(",")        
num1=int(list1[0])
num2=int(list1[1])
result1=""
for j in range(num1,num2+1,1):    
    for i in range(1,11,1):
        result1=str(j)+"*"+str(i)+"="+str(j*i) 
        print(result1)
        f2.write(result1)
        f2.write("\n")
    print()
    f2.write("\n")
f2.close()    

