#4 minutes, very slow
def allOdd(x):
    while x>0:
        if x%10%2==0:
            return False
        x//=10
    return True
def reverse(n):
    return int(str(n)[::-1])
count=0
for x in range(1,1_000_000_000):
    if x%10!=0:
        if allOdd(x+reverse(x)):
            count+=1
print(count)
