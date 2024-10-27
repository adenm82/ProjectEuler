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
def truncatable(x,dict):
    s=str(x)
    while len(s)>0:
        if int(s) in dict or int(s)<2:
            return False
        s=s[:-1]
    s=str(x)
    while len(s)>0:
        if int(s) in dict or int(s)<2:
            return False
        s=s[1:]
    return True
dict=sieve(1_000_000)
primes=[x for x in range(2,1_000_000) if x not in dict]
truncs=[]
sum=0
index=0
while len(truncs)<11:
    if truncatable(primes[index],dict) and primes[index]>=10:
        truncs.append(primes[index])
        sum+=primes[index]
    index+=1
print(sum)
