def digitalSum(x):
    sum=0
    for digit in str(x):
        sum+=int(digit)
    return sum
maxSum=0
for a in range (1,100):
    for b in range(1,100):
        maxSum=max(maxSum,digitalSum(a**b))
print(maxSum)
