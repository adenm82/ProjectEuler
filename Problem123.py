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
dict=sieve(10_000_000)
primes=[]
for x in range(2,10_000_000):
    if x not in dict:
        primes.append(x)
print(len(primes))
for i,x in enumerate(primes):
    n=i+1
    t1=(x-1)**n
    t2=(x+1)**n
    rem=(t1+t2)%(x**2)
    if rem>10**10:
        print(n)
        break
print("Done")
