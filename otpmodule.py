import random
import math
def generateotp(size,count):
    list1=[]
    for i in range(0,count,1):    
        otp1=random.randint(int(math.pow(10,size-1)),int(math.pow(10,size))-1)
        list1.append(otp1)
    return list1

def square(num1):
    return num1*num1


