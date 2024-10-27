count=0
for x in range(1,10000):
    for y in range(1,100):
        power=int(x**y)
        if len(str(power))==y:
            count+=1
            print(x,y,x**y)
print(count)
