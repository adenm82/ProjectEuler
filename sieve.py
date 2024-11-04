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
num=1_000_000
dict=sieve(num)
primes=[x for x in range(2,num) if x not in dict]
