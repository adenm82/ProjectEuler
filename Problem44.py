pents=[]
for x in range(1,5000):
    pents.append(int(x*((3*x)-1)/2))
diff=float('inf')
p1=0
p2=0
for x in range(len(pents)):
    for y in range(x+1,len(pents)):
        if y==x+1 and x%100==0:
            print(x)
        if pents[x]+pents[y] in pents and abs(pents[x]-pents[y]) in pents:
            if abs(pents[x]-pents[y])<diff:
                diff=abs(pents[x]-pents[y])
                p1=pents[x]
                p2=pents[y]
print(diff,p1,p2)
