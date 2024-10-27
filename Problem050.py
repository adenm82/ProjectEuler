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
dict=sieve(1_000_000)
primes=[x for x in range(2,1_000_000) if x not in dict]
print(primes[-5:])
maxNum=0
maxLength=0
for x in range(len(primes)):
    sum=primes[x]
    for y in range(x+1,len(primes)):
        sum+=primes[y]
        if sum>1_000_000:
            sum-=primes[y]
            break
    if sum not in dict:
        if y-x>maxLength:
            maxLength=y+1
            maxNum=sum
print(maxNum,maxLength)
