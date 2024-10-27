def sumOfFifths(x):
    sum=0
    for dig in str(x):
        sum+=int(dig)**5
    return sum==x
sum=0
for x in range(2,1000000):
    if sumOfFifths(x):
        sum+=x
print(sum)
