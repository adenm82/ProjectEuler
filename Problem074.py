def fac(x):
    prod=1
    for x in range(1,x+1):
        prod*=x
    return prod
def facDigs(x):
    s=str(x)
    sum=0
    for y in s:
        sum+=fac(int(y))
    return sum
def cycle(x):
    arr=[x]
    while facDigs(x) not in arr:
        arr.append(facDigs(x))
        x=facDigs(x)
    end=facDigs(x)
    return len(arr)
count=0
for x in range(1,1000000):
    print(x)
    if cycle(x)==60:
        count+=1
print(count)
