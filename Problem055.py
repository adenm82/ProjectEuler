def lychrel(x):
    count=0
    while count<50:
        x+=int(str(x)[::-1])
        if x==int(str(x)[::-1]):
            return False
        count+=1
    return True
count=0
for x in range(1,10000):
    if lychrel(x):
        count+=1
print(count)
