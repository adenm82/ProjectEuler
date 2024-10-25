def isBouncy(n):
    s=str(n)
    l=False
    m=False
    for x in range(1,len(s)):
        if int(s[x])<int(s[x-1]):
            l=True
        if int(s[x])>int(s[x-1]):
            m=True
    return l==True and m==True
count=0
prop=0
x=1
while True:
    if isBouncy(x):
        count+=1
    prop=count/x
    if prop==0.99:
        print(x)
        break
    x+=1
