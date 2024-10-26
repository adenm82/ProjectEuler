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
dict=sieve(1000000)
primes=[x for x in range(2,1_000_000) if x not in dict]
num=600851475143
maxFactor=0
while num>1:
    for x in primes:
        if num%x==0:
            maxFactor=max(maxFactor,x)
            num//=x
print(maxFactor)
