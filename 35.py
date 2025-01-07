f1=open("dictionary.txt","r")
list1=f1.readlines()
list2=[]
len1=len(list1)
for i in range(0,len1,1):    
    s1=list1[i].strip()
    list2.append(s1)


list3=[]
for ele in list1:
    print(ele)
    s1=ele.strip()
    list3.append(s1)
