tribonacci=[1,1,1]
for x in range(25000):
    tribonacci.append(tribonacci[-1]+tribonacci[-2]+tribonacci[-3])
count=0
nums=[]
tf=True
for x in range(1,2500,2):
    if x%201==0:
        print(x)
    tf=True
    for y in tribonacci:
        if y%x==0:
            tf=False
    if tf:
        count+=1
        nums.append(x)
print(nums[123])
