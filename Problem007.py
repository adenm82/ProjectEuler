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
numPrime=0
x=2
while numPrime<10001:
    if x not in dict:
        numPrime+=1
    x+=1
print(x-1)
