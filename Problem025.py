n1=1
n2=1
fib=2
index=4
while len(str(fib))<1000:
    temp=n2
    n1=n2
    n2=fib
    fib+=temp
    index+=1
print(index-1)
