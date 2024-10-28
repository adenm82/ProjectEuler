def factors(x):
    facs=set()
    for i in range(1,x//2+1):
        if x%i==0:
            if i in facs:
                return len(facs)
            facs.add(i)
            facs.add(x//i)
    return len(facs)
n=2
tri=3
while factors(tri)<=500:
    n+=1
    tri+=n
print(tri)
