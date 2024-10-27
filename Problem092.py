def squareDigits(x):
    sum=0
    for digit in str(x):
        sum+=int(digit)**2
    return sum
def chain(x):
    while x!=89 and x!=1:
        x=squareDigits(x)
    return x==89
count=0
for x in range(1,10_000_000):
    if chain(x):
        count+=1
print(count)
