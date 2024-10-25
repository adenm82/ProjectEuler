def sumDigs(x):
    sum=0
    for y in str(x):
        sum+=int(y)
    return sum
def any(num):
    sum=sumDigs(num)
    if sum==1:
        return False
    power=1
    while sum**power<num:
        power+=1
    if sum**power==num:
        return [sum,power,num]
    return []
dict={}
arr=[]
for x in range(1,200):
    for y in range(1,40):
        if x**y>=10:
            num=sumDigs(int(x**y))
            if num==x:
                arr.append(x**y)
arr.sort()
print(arr[29])
