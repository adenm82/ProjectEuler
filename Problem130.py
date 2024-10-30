#Very slow, might look for better solution
import sys
def gcd10(x):
    nums=[2,5,10]
    for y in nums:
        if x%y==0:
            return False
    return True
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
def R(k):
    s=""
    for x in range(k):
        s+='1'
    return int(s)
def A(n):
    k=1
    while not R(k)%n==0:
        k+=1
    return k
sys.set_int_max_str_digits(100_000)
dict=sieve(100_000)
comps=[x for x in range(2,100_000) if x in dict and gcd10(x)]
sum=0
c=[]
for x in comps:
    if (x-1)%(A(x))==0:
        sum+=x
        c.append(x)
        if len(c)==25:
            break
print(sum)
