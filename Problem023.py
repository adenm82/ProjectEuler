def factors(x):
    facs=set()
    sum=0
    for i in range(1,x//2+1):
        if x%i==0:
            if i in facs:
                break
            sum+=i
            if i!=x//i:
                sum+=x//i
            facs.add(i)
            facs.add(x//i)
    return sum-x
def abundant(x):
    return factors(x)>x
abuns=[]
for x in range(10,28124):
    if abundant(x):
        abuns.append(x)
nums=set()
for x in abuns:
    for y in abuns:
        nums.add(x+y)
sum=0
for x in range(28124):
    if x not in nums:
        sum+=x
print(sum)
