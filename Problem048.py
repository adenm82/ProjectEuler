sum=0
for x in range(1,1001):
    sum+=x**x
    if len(str(sum))>10:
        sum=int(str(sum)[-10:])
print(sum)
