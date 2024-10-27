def isPrime(n):
    if n<2:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True
def isCircular(n):
    s=str(n)
    if "0" in s or "2" in s or "4" in s or "6" in s or "8" in s:
        return False
    for x in range(len(s)-1):
        s=s[-1]+s[:-1]
        if not isPrime(int(s)):
            return False
    return True
count=0
for x in range(1000000):
    if x%10000==0:
        print(x)
    if isPrime(x):
        if isCircular(x):
            count+=1
print(count)
