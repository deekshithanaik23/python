import random

def generateotp(length,size):    
    rand1=""
    list1=[]
    for j in range(0,size,1):    
        for i in range(0,length,1):
            num1=random.randrange(0,10)
            rand1=rand1+str(num1)
        list1.append(rand1)
        rand1=""
    return list1
print(generateotp(4,10))
