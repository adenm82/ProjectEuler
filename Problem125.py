def isPal(x):
    s=str(x)
    l=len(s)//2
    s1=s[:l]
    if len(s)%2==0:
        s2=s[l:]
    else:
        s2=s[l+1:]
    for x in range(len(s1)):
        if s1[x]!=s2[len(s1)-x-1]:
            return False
    return True
squares=[]
sum=0
for x in range(1,10000):
    squares.append(x**2)
arr=[]
for x in range(len(squares)):
    sum=squares[x]
    for y in range(x+1,len(squares)):
        sum+=squares[y]
        if sum<100_000_000:
            if isPal(sum):
                arr.append(sum)
sum=0
for x in list(set(arr)):
    sum+=x
print(sum)
