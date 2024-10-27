def sieve(num):
    prime = [True for i in range(num+1)]
    dict={}
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
                dict[i]=0
        p += 1
    return dict
dict=sieve(100000)
bs=[x for x in range(2,1001) if x not in dict]
dict[0]=1
dict[1]=1
maxPrimes=0
maxa=0
maxb=0
for a in range(-999,1000):
    print(a)
    for b in bs:
        count=0
        n=0
        while True:
            eq=(n**2)+(a*n)+b
            if eq not in dict and eq>0:
                count+=1
            else:
                break
            n+=1
        if count>maxPrimes:
            maxPrimes=count
            maxa=a
            maxb=b
print(maxa*maxb)
        
