def isPrime(n):
    if n<2:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True
def isPermute(x,y):
    dictx={}
    dicty={}
    for d1 in str(x):
        if d1 in dictx:
            dictx[d1]+=1
        else:
            dictx[d1]=1
    for d2 in str(y):
        if d2 in dicty:
            dicty[d2]+=1
        else:
            dicty[d2]=1
    return dictx==dicty
for x in range(1000,3440):
    x1=x+3330
    x2=x+6660
    if isPrime(x) and isPrime(x1) and isPrime(x2):
        if isPermute(x,x1) and isPermute(x1,x2):
            print(x,x1,x2)
