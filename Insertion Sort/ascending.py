n=20000
fp = open("ascending_"+str(n)+".txt","w")
fp.write(str(n)+" ")  
for i in range(1,n+1):
    fp.write(str(i)+" ")  
fp.close()
