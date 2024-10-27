def minarr(arr):
    Min=float('inf')
    for x in arr:
        Min=min(Min,x)
    return Min
def Props(num) :
    result = 0
    i = 2
    while i<=num**0.5:
        if (num % i == 0) :
            if (i == (num / i)) :
                result = result + i
            else :
                result = result +  (i + num/i)
        i = i + 1
    return (result + 1)
def chain(x):
    arr=set()
    arr.add(x)
    start=x
    while Props(x) not in arr:
        if x>1000000:
            return []
        arr.add(Props(x))
        x=Props(x)
    if Props(x)==start:
        return list(arr)
    return []
maxChain=[]
maxLength=0
for x in range(1,20_000):
    ch=chain(x)
    if len(ch)>maxLength:
        maxChain=ch
        maxLength=len(ch)
print(maxChain)
print(maxLength)
