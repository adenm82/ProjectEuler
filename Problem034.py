def fac(x):
    if x<=1:
        return 1
    return x*fac(x-1)
def isSum(x):
    sum=0
    for digit in str(x):
        sum+=fac(int(digit))
    return sum==x
sum=0
for x in range(3,50000):
    if isSum(x):
        sum+=x
print(sum)
