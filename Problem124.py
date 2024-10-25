def isPrime(n):
    if n<2:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True
def rad(n,primes):
    arr=[]
    while n>1:
        for x in primes:
            if n%x==0:
                n/=x
                arr.append(x)
    arr=list(set(arr))
    prod=1
    for x in arr:
        prod*=x
    return prod
primes=[]
for x in range(100000):
    if isPrime(x):
        primes.append(x)
print("Done")
dict={}
arr=[]
for x in range(1,100001):
    if x%100==0:
        print(x)
    if rad(x,primes) in dict:
        dict[rad(x,primes)].append(x)
    else:
        dict[rad(x,primes)]=[x]
    arr.append(rad(x,primes))
arr.sort()
print(dict[arr[9999]])
