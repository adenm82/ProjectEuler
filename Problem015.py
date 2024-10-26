def collatz(x):
    chain=1
    num=x
    while x>1:
        if x%2==0:
            x//=2
        else:
            x=3*x+1
        chain+=1
    return [chain,num]
maxChain=0
maxNum=0
for x in range(1,1_000_000):
    col=collatz(x)
    if col[0]>maxChain:
        maxChain=col[0]
        maxNum=col[1]
print(maxNum)
