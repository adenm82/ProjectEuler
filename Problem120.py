def r(a,n):
    return (((a-1)**n)+((a+1)**n))%(a*a)
sum=0
most=0
for x in range(3,1001):
    print(x)
    most=0
    for y in range(2000):
        most=max(most,r(x,y))
    sum+=most
print(sum)
