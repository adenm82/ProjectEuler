def Props(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum+=x
    return sum
def isAmicable(x):
    y=Props(x)
    if x==y:
        return False
    return Props(y)==x
sum=0
for x in range(10000):
    if isAmicable(x):
        sum+=x
print(sum)
