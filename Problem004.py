maxNum=0
for x in range(100,1000):
    for y in range(100,1000):
        product=x*y
        if str(product)==str(product)[::-1]:
            maxNum=max(product,maxNum)
print(maxNum)
