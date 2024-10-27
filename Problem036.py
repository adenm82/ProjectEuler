sum=0
for x in range(1,1_000_000):
    b2="{0:b}".format(x)
    b10=x
    if b2==b2[::-1] and b10==int(str(b10)[::-1]):
        sum+=x
print(sum)
