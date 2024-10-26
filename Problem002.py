sum=0
n1=1
n2=1
fib=2
while fib<4_000_000:
    if fib%2==0:
        sum+=fib
    temp=fib+n2
    n1=n2
    n2=fib
    fib=temp
print(sum)
