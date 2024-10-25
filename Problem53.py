def factorial(n):
    product=1
    for x in range(1,n+1):
        product*=x
    return product
def choose(n,r):
    nf=factorial(n)
    rf=factorial(r)
    nmrf=factorial(n-r)
    return int(nf/(rf*nmrf))
count=0
for n in range(1,101):
    for r in range(1,n+1):
        if choose(n,r)>1000000:
            count+=1
print(count)
