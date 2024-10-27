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
dict=sieve(10000)
primes=[x for x in range(2,10000) if x not in dict]
nums=set()
for x in primes:
    for y in range(1,1000):
        nums.add(x+(2*(y**2)))
x=2
while x in nums or x not in dict or x%2==0:
    x+=1
print(x)
