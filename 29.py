for j in range(0,12,1):    
    for i in range(0,12,1):
        time1=str(9+j)+":"+str(i*5).zfill(2)
        angle1=(90-30*j)+30*i-i*2.5
        print(time1+" - "+str(angle1%360))
    print()


