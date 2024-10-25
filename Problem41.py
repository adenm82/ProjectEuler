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
def isPan(n):
    l=len(str(n))
    nums="123456789"
    for x in range(l):
        if nums[x] not in str(n):
            return False
    return True
dict=sieve(10000000)
for x in range(10000000):
    if isPan(x) and x not in dict:
        print(x)
