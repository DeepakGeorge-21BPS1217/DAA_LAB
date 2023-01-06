import random
n = 30000
fp = open("random_"+str(n)+".txt","w")
fp.write(str(n)+" ")  
for i in range(1,n+1):
    x = random.random()
    fp.write(str(int(x*n))+" ")
x = random.random() 
fp.close()
