from collections import Counter
def isPan(x):
    c=Counter("123456789")
    return c==Counter(x)
sum=0
prods=set()
for x in range(2500):
    for y in range(2500):
        prod=x*y
        concat=str(x)+str(y)+str(prod)
        if isPan(concat):
            if prod not in prods:
                sum+=prod
                prods.add(prod)
print(sum)
