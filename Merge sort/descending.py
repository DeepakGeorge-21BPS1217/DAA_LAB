n=30000
fp = open("descending_"+str(n)+".txt","w")
fp.write(str(n)+" ")  
for i in range(n-1,0,-1):
    fp.write(str(i)+" ")  
fp.close()
