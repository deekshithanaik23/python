import os
import datetime as dt
today=dt.datetime.now()
dir1="TABLES"
os.mkdir(dir1)
os.chdir(dir1)
start=10
end=20
result1=""
for j in range(start,end+1,1):
    part1=str(j)
    part2=today.strftime("_%Y%m%d_%H%M%S")
    part3=".txt"
    fname=part1+part2+part3
    f2=open(fname,"w")
    for i in range(1,11,1):
        info1=str(j)+"*"+str(i)+"="+str(j*i)
        print(info1)
        f2.write(info1+"\n")
    print()
    f2.close()
