s=""
x=1
while len(s)<1_000_000:
    s+=str(x)
    x+=1
nums=[s[0],s[9],s[99],s[999],s[9999],s[99999],s[999999]]
product=1
for x in nums:
    product*=int(x)
print(product)
