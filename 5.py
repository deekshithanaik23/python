def calc(num1,num2):
    

    sum1=num1+num2
    dif1=num1-num2
    mul1=num1*num2
    div1=num1/num2
    div2=num1//num2
    rem1=num1%num2
    exp1=num1**num2
    result=(str(sum1)+" "+str(dif1)+" "+str(mul1)+" "+str(div1)+" "+str(div2)+" "+str(rem1)+" "+str(exp1))
    return result 
f1=open("in1.txt","r")
f2=open("out1.txt","w")
num1=int(f1.readline())
num2=int(f1.readline())
result=calc(num1,num2)
print(result)
f2.write(result)
f2.close()












