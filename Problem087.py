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
dict=sieve(int(50_000_000**0.5))
squares=[]
cubes=[]
fourths=[]
for x in range(2,int(50_000_000**0.5)):
    if x not in dict:
        squares.append(x**2)
        if x<50_000_000**(1/3):
            cubes.append(x**3)
        if x<50_000_000**0.25:
            fourths.append(x**4)
arr=[]
for x in squares:
    for y in cubes:
        for z in fourths:
            if x+y+z<50_000_000:
                arr.append(x+y+z)
print(len(list(set(arr))))
