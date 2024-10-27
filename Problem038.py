from collections import Counter
def isPan(x):
    c=Counter("123456789")
    return c==Counter(str(x))
largest=0
for x in range(10000):
    num=str(x)
    mult=2
    while len(num)<9:
        num+=str(x*mult)
        mult+=1
    if isPan(int(num)):
        largest=max(largest,int(num))
print(largest)
